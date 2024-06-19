from shapediver.geometry_api_v2 import SdClient, sd_utils
from shapediver.geometry_api_v2.client import (
    Configuration,
    ReqSdtfDefinition,
    ReqSdtfType,
    SdtfApi,
    SessionApi,
)


def test_sdtf(utils, host, jwt_model):
    model_client = SdClient(Configuration(host, access_token=jwt_model))
    client = SdClient(Configuration(host))
    namespace = "pub"

    # Initialize a new session.
    ticket = utils.create_ticket()
    res_session = SessionApi(client).create_session_by_ticket(ticket)
    session_id = res_session.session_id
    assert res_session.parameters

    # sdTF upload.
    with open("tests/data/test.sdtf", "rb") as f:
        s = f.read()

        # Request a sdTF upload for a specific namespace.
        res_upload = SdtfApi(client).upload_sdtf(
            session_id,
            [
                ReqSdtfDefinition(
                    content_length=len(s),
                    content_type=ReqSdtfType.MODEL_SLASH_VND_DOT_SDTF,
                    namespace=namespace,
                )
            ],
        )
        sdtf = res_upload.asset.sdtf[0]
        assert sdtf

        # Upload the sdTF.
        upload = sd_utils.upload(sdtf.href, s, ReqSdtfType.MODEL_SLASH_VND_DOT_SDTF)
        assert upload.status == 200

    # Download the uploaded sdTF.
    res_data = SdtfApi(model_client).download_sdtf(session_id, namespace, sdtf.id)
    assert len(res_data) > 0

    # List all sdTFs of a specific namespace.
    res_list = SdtfApi(model_client).list_sdtfs(session_id, namespace)
    assert len(res_list.list.sdtf) > 0

    # Delete the uploaded sdTF.
    SdtfApi(model_client).delete_sdtf(session_id, namespace, sdtf.id)

    # Close the session.
    SessionApi(client).close_session(session_id)
