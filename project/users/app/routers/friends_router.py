from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi_utils.cbv import cbv

from app.models.users.user_create import UserCreate
from app.models.users.user_details import User
from app.repositories.friends_repository import FriendsRepository
from app.repositories.users_repository import UsersRepository
from app.services.friends.friends_service import FriendsService
from app.services.users.users_service import UsersService
from app.db.db import get_db
from app.shared.decorators.auth_required import auth_current_user
from app.shared.helpers.crypt_helper import CryptHelper
from app.shared.service_result import handle_result

router = APIRouter()


def get_friends_service(db: Session = Depends(get_db)):
    return FriendsService(
        db,
        FriendsRepository(db)
    )


@cbv(router)
class UsersRouter:

    __db: Session = Depends(get_db)
    __service: FriendsService = Depends(get_friends_service)

    @router.put("/{friend_id}")
    async def make_friendship(
            self,
            friend_id: int,
            current_user: User = Depends(auth_current_user)
    ):
        result = self.__service.add_friend(current_user.id, friend_id)
        return handle_result(result)