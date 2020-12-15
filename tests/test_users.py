import pytest
from api.reqres_api_client import ReqresApiClient


@pytest.mark.smoke
@pytest.mark.user
@pytest.mark.get_user
def test_it_checks_user_list():
    users = ReqresApiClient.list_users()
    assert users["per_page"] == len(users["data"])


@pytest.mark.regression
@pytest.mark.user
@pytest.mark.post
def test_it_checks_user_created():
    user_details = {"name": "morpheus", "job": "leader"}
    user = ReqresApiClient.create_user(user_details)
    assert user_details["name"] == user["name"] and user_details["job"] == user["job"]


@pytest.mark.smoke
@pytest.mark.user
@pytest.mark.put
def test_it_checks_user_updated():
    user_details = {"name": "morpheus", "job": "zion resident"}
    user = ReqresApiClient.update_user(user_details)
    assert user_details["name"] == user["name"] and user_details["job"] == user["job"]


@pytest.mark.regression
@pytest.mark.user
@pytest.mark.delete
def test_it_checks_user_deleted():
    response = ReqresApiClient.delete_user()
    assert response.status_code == 204


@pytest.mark.regression
@pytest.mark.user
def test_it_registers_user():
    user_details = {"email": "eve.holt@reqres.in", "password": "pistol"}
    response = ReqresApiClient.register(user_details)
    assert response == {"id": 4, "token": "QpwL5tke4Pnpja7X4"}


@pytest.mark.smoke
@pytest.mark.user
def test_it_logins_user():
    user_details = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    response = ReqresApiClient.login(user_details)
    assert response == {"token": "QpwL5tke4Pnpja7X4"}
