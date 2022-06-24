import os

import requests
from sqlalchemy.util import namedtuple

from app.services.auth.auth_exception import AuthException
from app.shared.app_request import AppRequest

user_service_url = os.getenv("USERS_SERVICE_HOST_URL")
AUTH_ENDPOINT = f'{user_service_url}/auth'


def auth_current_user(request: AppRequest):
    token = request.headers.get("Authorization")
    if not token:
        raise AuthException.WrongToken()
    response = requests.get(
        AUTH_ENDPOINT,
        headers={"Authorization": token}
    )
    response.raise_for_status()
    dict = response.json()
    user = namedtuple("User", dict.keys())(*dict.values())
    if not user:
        raise AuthException.WrongToken()
    return user
