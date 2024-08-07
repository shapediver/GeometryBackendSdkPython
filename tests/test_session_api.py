from datetime import timedelta

from shapediver.geometry_api_v2.client import (
    Configuration,
    ReqTicket,
    ReqTicketType,
    SessionApi,
)
from shapediver.geometry_api_v2.sd_client import SdClient


def test_init_session_via_ticket(utils, host, jwt_backend, model_id):
    backend_client = SdClient(Configuration(host, access_token=jwt_backend))
    client = SdClient(Configuration(host))

    # Create new ticket that allows to initialize a new session.
    req_ticket = ReqTicket(
        pub=True,
        author=True,
        type=ReqTicketType.BACKEND,
        until=utils.now(timedelta(minutes=2)),
        use_id2=False,
    )
    res_ticket = SessionApi(backend_client).create_ticket(model_id, req_ticket)
    assert res_ticket.ticket is not None

    # Initialize a new session using the ticket.
    session_id = (
        SessionApi(client).create_session_by_ticket(res_ticket.ticket).session_id
    )
    assert session_id is not None

    # Get the session defaults.
    res_defaults = SessionApi(client).get_session_defaults(session_id)
    assert res_defaults.session_id == session_id

    # Close the session.
    SessionApi(client).close_session(session_id)


def test_init_session_via_model(host, jwt_backend, model_id):
    backend_client = SdClient(Configuration(host, access_token=jwt_backend))
    client = SdClient(Configuration(host))

    # Initialize a new session using the model ID.
    session_id = SessionApi(backend_client).create_session_by_model(model_id).session_id
    assert session_id is not None

    # Get the session defaults.
    res_defaults = SessionApi(client).get_session_defaults(session_id)
    assert res_defaults.session_id == session_id

    # Close the session.
    SessionApi(client).close_session(session_id)


def test_decrypt_ticket(utils, host, jwt_backend, model_id):
    backend_client = SdClient(Configuration(host, access_token=jwt_backend))

    # Create new ticket that allows to initialize a new session.
    req_ticket = ReqTicket(
        pub=True,
        author=True,
        type=ReqTicketType.BACKEND,
        until=utils.now(timedelta(minutes=2)),
        use_id2=False,
    )
    res_ticket = SessionApi(backend_client).create_ticket(model_id, req_ticket)
    assert res_ticket.ticket is not None

    # Decrypt the ticket.
    decrypted_ticket = (
        SessionApi(backend_client).decrypt_ticket(res_ticket.ticket).decrypted_ticket
    )
    assert decrypted_ticket.pub == req_ticket.pub
    assert decrypted_ticket.author == req_ticket.author
    assert decrypted_ticket.type == req_ticket.type
    assert decrypted_ticket.until == req_ticket.until
    assert decrypted_ticket.use_id2 == req_ticket.use_id2
