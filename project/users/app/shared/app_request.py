from starlette.requests import Request

from app.models.users.user_details import User


class AppRequest(Request):
    current_user: User

