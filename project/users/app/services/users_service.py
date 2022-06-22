from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app import models
from app.models.users.user_create import UserCreate
from app.repositories.users_repository import UsersRepository
from app.shared.base_service import BaseService
from app.shared.service_result import ServiceResult


class UsersService(BaseService):
    def __init__(self, db: Session, users_repository: UsersRepository, oauth: OAuth2PasswordBearer):
        super().__init__(db)
        self.users_repository = users_repository
        self.oauth = oauth

    def create_user(self, user: UserCreate) -> ServiceResult:
        new_user = self.users_repository.add_user(user)
        return ServiceResult(new_user)

    def get_user(self, user_id: int) -> ServiceResult:
        user = self.users_repository.get_user(user_id)
        return ServiceResult(user)

    def get_user_by_email(self, user_email: str) -> ServiceResult:
        user = self.users_repository.get_user_by_email(user_email)
        return ServiceResult(user)

    def get_user_by_token(self, token):
        return 0
