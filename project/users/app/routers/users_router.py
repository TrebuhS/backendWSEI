from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.models.users.user_create import UserCreate
from app.repositories.users_repository import UsersRepository
from app.services.auth.auth_service import AuthService
from app.services.users.users_service import UsersService
from app.db.db import get_db
from app.shared.app_request import AppRequest
from app.shared.decorators.auth_required import auth_required
from app.shared.helpers.crypt_helper import CryptHelper

router = APIRouter()


def get_users_service(db: Session = Depends(get_db)):
    return UsersService(
        db,
        UsersRepository(db),
        CryptHelper()
    )


@router.post("/")
def create_user(
        user: UserCreate,
        service=Depends(get_users_service)
):
    return service.create_user(user)


@router.get("/current")
@auth_required
async def get_current_user(
        request: AppRequest
):
    return request.current_user


@router.get("/{user_id}")
def get_user(
        user_id: int,
        service: UsersService = Depends(get_users_service)
):
    return service.get_user(user_id)


@router.get("/email/{user_email}")
def get_user(
        user_email: str,
        service: UsersService = Depends(get_users_service)
):
    return service.get_user_by_email(user_email)
