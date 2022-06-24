from sqlalchemy.orm import Session

from app.repositories.tags_repository import FriendsRepository
from app.services.users.user_exception import UserException
from app.shared.base_service import BaseService
from app.shared.service_result import ServiceResult


class FriendsService(BaseService):
    def __init__(
            self,
            db: Session,
            friends_repository: FriendsRepository
    ):
        super().__init__(db)
        self.__friends_repository = friends_repository

    def add_friend(self, current_user_id: id, friend_id: id) -> ServiceResult:
        self.__friends_repository.add_friendship(current_user_id, friend_id)
        return ServiceResult(True)