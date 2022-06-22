from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic.decorator import wraps
from sqlalchemy.orm import Session
from starlette.requests import Request

from app.models.users.user_create import UserCreate
from app.models.users.user_details import User
from app.repositories.users_repository import UsersRepository
from app.services.users_service import UsersService
from app.db.db import get_db
from app.shared.app_request import AppRequest
from app.shared.decorators.auth_required import auth_required

router = APIRouter()


def get_users_service(db: Session = Depends(get_db)):
    return UsersService(db, UsersRepository(db), OAuth2PasswordBearer(tokenUrl="/auth"))


@router.get("/auth")
async def verify_token(
        service=Depends(get_users_service)
):
    return service.verify_token()


@router.post("/")
def create_user(
        user: UserCreate,
        service=Depends(get_users_service)
):
    return service.create_user(user)


@router.get("/current")
@auth_required
def get_current_user(
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
