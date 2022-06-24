from sqlalchemy.orm import Session

from app.models.users.user_create import UserCreate
from app.repositories.users_repository import UsersRepository
from app.services.users.user_exception import UserException
from app.shared.base_service import BaseService
from app.shared.helpers.crypt_helper import CryptHelper
from app.shared.service_result import ServiceResult


class UsersService(BaseService):
    def __init__(
            self,
            db: Session,
            users_repository: UsersRepository,
            crypt_helper: CryptHelper
    ):
        super().__init__(db)
        self.__users_repository = users_repository
        self.__crypt_helper = crypt_helper

    def create_user(self, user: UserCreate) -> ServiceResult:
        user.password = self.__crypt_helper.get_password_hash(user.password)
        new_user = self.__users_repository.add_user(user)
        if not new_user:
            return ServiceResult(UserException.WrongUserData())
        return ServiceResult(new_user)

    def get_user(self, user_id: int) -> ServiceResult:
        user = self.__users_repository.get_user(user_id)
        if not user:
            return ServiceResult(UserException.NotFound())
        return ServiceResult(user)

    def get_user_by_email(self, user_email: str) -> ServiceResult:
        user = self.__users_repository.get_user_by_email(user_email)
        if not user:
            return ServiceResult(UserException.NotFound())
        return ServiceResult(user)
