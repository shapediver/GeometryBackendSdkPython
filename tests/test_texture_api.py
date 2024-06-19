from shapediver.geometry_api_v2.client import Configuration, SessionApi, TextureApi
from shapediver.geometry_api_v2.sd_client import SdClient


def test_textures(utils, host, jwt_model):
    model_client = SdClient(Configuration(host, access_token=jwt_model))

    # Initialize a new session.
    ticket = utils.create_ticket()
    session_id = SessionApi(model_client).create_session_by_ticket(ticket).session_id

    # List all model textures.
    res_list = TextureApi(model_client).list_textures(session_id)
    print(f"res_list: {res_list}")
    assert res_list.list.texture is not None

    # Close the session.
    SessionApi(model_client).close_session(session_id)
