import time
from datetime import datetime, timedelta, timezone

from shapediver.geometry_api_v2 import (
    Configuration,
    ModelApi,
    QueryOrder,
    SdClient,
    SessionAnalyticsStatus,
    SessionApi,
)


def _date_time_ms(diff_seconds=0):
    # Analytics bounds are 17-digit UTC; ticket expiry uses Utils.now (14 digits).
    current = datetime.now(timezone.utc) + timedelta(seconds=diff_seconds)
    return current.strftime("%Y%m%d%H%M%S") + f"{current.microsecond // 1000:03d}"


def _sole_session(sessions, session_id):
    revealed = [row for row in sessions if row.id == session_id]
    if len(revealed) == 1:
        return revealed[0]
    if len(revealed) > 1:
        raise ValueError(f"multiple analytics rows for session {session_id}")
    redacted = [row for row in sessions if row.id == "<redacted>"]
    if len(redacted) == 1:
        return redacted[0]
    raise ValueError(
        f"expected one analytics row for session {session_id}, "
        f"found {len(revealed)} revealed and {len(redacted)} redacted"
    )


def _until_row(load, accept):
    for attempt in range(8):
        try:
            value = load()
            accept(value)
            return value
        except Exception:
            if attempt == 7:
                raise
            time.sleep(1)


def _close_once(session_api, session_id, state):
    if state["closed"]:
        return
    session_api.close_session(session_id)
    # Set only after close_session returns so finally can retry a failed close.
    state["closed"] = True


def test_model_sessions_analytics(utils, host, jwt_model, model_id):
    model_client = SdClient(Configuration(host, access_token=jwt_model))
    client = SdClient(Configuration(host))
    model_api = ModelApi(model_client)
    session_api = SessionApi(client)

    timestamp_from = _date_time_ms(-60)
    ticket = utils.create_ticket()
    session_id = session_api.create_session_by_ticket(ticket).session_id
    timestamp_to = _date_time_ms(60)
    state = {"closed": False}

    def load():
        return model_api.get_model_sessions_analytics(
            model_id,
            order=QueryOrder.DESC,
            timestamp_from=timestamp_from,
            timestamp_to=timestamp_to,
            limit=20,
        )

    try:
        def accept_open(page):
            row = _sole_session(page.sessions, session_id)
            if row.status != SessionAnalyticsStatus.OPEN:
                raise ValueError(f"session {session_id} is {row.status}")

        open_page = _until_row(load, accept_open)
        assert (
            _sole_session(open_page.sessions, session_id).status
            == SessionAnalyticsStatus.OPEN
        )

        _close_once(session_api, session_id, state)

        def accept_pending(page):
            row = _sole_session(page.sessions, session_id)
            if row.status != SessionAnalyticsStatus.PENDING:
                raise ValueError(f"session {session_id} is {row.status}")

        pending_page = _until_row(load, accept_pending)
        pending = _sole_session(pending_page.sessions, session_id)
        assert pending.status == SessionAnalyticsStatus.PENDING
        assert pending.id == session_id
    finally:
        _close_once(session_api, session_id, state)
