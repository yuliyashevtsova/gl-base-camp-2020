import requests
from urllib.parse import urljoin
from config.config import Config
from endpoints.endpoints import Endpoints


class ReqresApiClient:
    @staticmethod
    def _prepare_url(url, base_url=Config.BASE_URL):
        return urljoin(base_url, url)

    @staticmethod
    def list_users():
        return requests.get(url=ReqresApiClient._prepare_url(Endpoints.USERS)).json()

    @staticmethod
    def create_user(user_details):
        return requests.post(
            url=ReqresApiClient._prepare_url(Endpoints.USER), json=user_details
        ).json()

    @staticmethod
    def update_user(user_details):
        return requests.put(
            url=ReqresApiClient._prepare_url(Endpoints.USER), json=user_details
        ).json()

    @staticmethod
    def delete_user():
        return requests.delete(url=ReqresApiClient._prepare_url(Endpoints.USER))

    @staticmethod
    def register(user_details):
        return requests.post(
            ReqresApiClient._prepare_url(Endpoints.REGISTER), json=user_details
        ).json()

    @staticmethod
    def login(user_details):
        return requests.post(
            ReqresApiClient._prepare_url(Endpoints.LOGIN), json=user_details
        ).json()
