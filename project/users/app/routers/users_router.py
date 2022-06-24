from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi_utils.cbv import cbv

from app.models.users.user_create import UserCreate
from app.models.users.user_details import User
from app.repositories.users_repository import UsersRepository
from app.services.users.users_service import UsersService
from app.db.db import get_db
from app.shared.decorators.auth_required import auth_current_user
from app.shared.helpers.crypt_helper import CryptHelper
from app.shared.service_result import handle_result

router = APIRouter()


def get_users_service(db: Session = Depends(get_db)):
    return UsersService(
        db,
        UsersRepository(db),
        CryptHelper()
    )


@cbv(router)
class UsersRouter:

    db: Session = Depends(get_db)
    service: UsersService = Depends(get_users_service)

    @router.post("/")
    async def create_user(
            self,
            user: UserCreate
    ):
        result = self.service.create_user(user)
        return handle_result(result)

    @router.get("/{user_id}")
    async def get_user(
            self,
            user_id: int,
            current_user: User = Depends(auth_current_user)
    ):
        result = self.service.get_user(user_id)
        return handle_result(result)

    @router.get("/email/{user_email}")
    async def get_user_by_email(
            self,
            user_email: str,
            current_user: User = Depends(auth_current_user)
    ):
        result = self.service.get_user_by_email(user_email)
        return handle_result(result)
