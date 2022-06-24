from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.db import get_db
from app.services.auth.auth_exception import AuthException
from app.shared.app_request import AppRequest


def auth_current_user(request: AppRequest, db: Session = Depends(get_db)):
    return request
