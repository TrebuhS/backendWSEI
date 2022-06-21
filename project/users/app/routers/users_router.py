from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.models.users.user_create import UserCreate
from app.repositories.users_repository import UsersRepository
from app.services.users_service import UsersService
from app.db.db import get_db

router = APIRouter()


def get_users_service(db: Session = Depends(get_db)):
    return UsersService(db, UsersRepository(db), OAuth2PasswordBearer(tokenUrl="/auth"))


@router.get("/auth")
def verify_token():
    return 1


@router.post("/")
def create_user(
        user: UserCreate,
        service=Depends(get_users_service)
):
    return service.create_user(user)


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
