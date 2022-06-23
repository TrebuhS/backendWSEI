from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.repositories.users_repository import UsersRepository
from app.services.auth.auth_service import AuthService
from app.db.db import get_db
from app.shared.helpers.crypt_helper import CryptHelper

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
        service=Depends(get_auth_service)
):
    return service.verify_token()


@router.post("/login")
async def login_for_access_token(
        form_data: OAuth2PasswordRequestForm = Depends(),
        service=Depends(get_auth_service)
):
    return service.login(form_data)
