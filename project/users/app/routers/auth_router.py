from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette.requests import Request

from app.repositories.users_repository import UsersRepository
from app.services.auth.auth_service import AuthService
from app.db.db import get_db
from app.shared.app_request import AppRequest
from app.shared.helpers.crypt_helper import CryptHelper
from app.shared.service_result import handle_result

router = APIRouter()


def get_auth_service(db: Session = Depends(get_db)):
    return AuthService(
        db,
        UsersRepository(db),
        OAuth2PasswordBearer("/login"),
        CryptHelper()
    )


@router.get("/")
async def verify_token(
        request: Request,
        service=Depends(get_auth_service)
):
    result = service.handle_token_verification(request)
    return handle_result(result)


@router.post("/login")
async def login_for_access_token(
        form_data: OAuth2PasswordRequestForm = Depends(),
        service=Depends(get_auth_service)
):
    result = service.login(form_data)
    return handle_result(result)
