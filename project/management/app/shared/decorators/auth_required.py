import os

import requests
from sqlalchemy.util import namedtuple

from app.shared.app_request import AppRequest
from app.shared.exceptions import AppExceptionCase

user_service_url = os.getenv("USERS_SERVICE_HOST_URL")
AUTH_ENDPOINT = f'{user_service_url}/auth'


def auth_current_user(request: AppRequest):
    token = request.headers.get("Authorization")
    if not token:
        raise AuthException.WrongToken()
    try:
        response = requests.get(
            AUTH_ENDPOINT,
            headers={"Authorization": token}
        )
        response.raise_for_status()
        dict = response.json()
        return namedtuple("User", dict.keys())(*dict.values())
    except:
        raise AuthException.WrongToken()


class AuthException:
    class WrongToken(AppExceptionCase):
        def __init__(self, context: dict = None):
            """
            Provided token is not correct.
            """
            status_code = 401
            AppExceptionCase.__init__(self, status_code, context)