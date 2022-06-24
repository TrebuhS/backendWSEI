from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.db import get_db
from app.routers.auth_router import get_auth_service
from app.services.auth.auth_exception import AuthException
from app.shared.app_request import AppRequest


def auth_current_user(request: AppRequest, db: Session = Depends(get_db)):
    auth_service = get_auth_service(db)
    user_result = auth_service.handle_token_verification(request)
    if not user_result.success:
        raise AuthException.WrongToken()
    return user_result.value
