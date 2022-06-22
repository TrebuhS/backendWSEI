from pydantic.decorator import wraps

from app.models.users.user_details import User
from app.shared.app_request import AppRequest


def auth_required(func):
    @wraps(func)
    async def wrapper(request: AppRequest = None, *args, **kwargs):
        if request:
            request.current_user = User(
                id=1,
                first_name="first",
                last_name="last",
                email="email",
                password="password"
            )
            return await func(request, *args, **kwargs)
        return await func(*args, **kwargs)
    return wrapper
