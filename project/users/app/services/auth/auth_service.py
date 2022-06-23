from typing import Union

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from pydantic.validators import timedelta, datetime
from sqlalchemy.orm import Session

from app.db.tables.user import User
from app.models.auth.token_data import TokenData
from app.repositories.users_repository import UsersRepository
from app.services.auth.auth_exception import AuthException
from app.shared.base_service import BaseService
from jose import jwt, JWTError

from app.shared.helpers.crypt_helper import CryptHelper
from app.shared.service_result import ServiceResult

SECRET_KEY = "ad78b0417be0e7b7f36660a0bc8393d0d043602f43ee358db753dd48410a6f4e"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class AuthService(BaseService):
    def __init__(
            self,
            db: Session,
            users_repository: UsersRepository,
            oauth: OAuth2PasswordBearer,
            crypt_helper: CryptHelper
    ):
        super().__init__(db)
        self.users_repository = users_repository
        self.oauth = oauth
        self.crypt_helper = crypt_helper



    def login(self, form_data: OAuth2PasswordRequestForm):
        user = self.users_repository.get_user_by_email(form_data.username)
        if not user:
            return ServiceResult(AuthException.IncorrectCredentials())
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = self.__create_access_token(
            data={"sub": user.id},
            expires_delta=access_token_expires
        )
        return ServiceResult({
            "access_token": access_token,
            "token_type": "bearer"
        })

    def authenticate_user(self, password: str, user: User):
        if not user:
            return False
        if not self.crypt_helper.verify_password(password, user.hashed_password):
            return False
        return user

    def __create_access_token(self, data: dict, expires_delta: Union[timedelta, None] = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    async def get_current_user(self):
        try:
            payload = jwt.decode(self.oauth, SECRET_KEY, algorithms=[ALGORITHM])
            id: int = payload.get("sub")
            if id is None:
                return ServiceResult(AuthException.WrongToken())
            token_data = TokenData(id=id)
        except JWTError:
            return ServiceResult(AuthException.WrongToken())
        user = self.users_repository.get_user(token_data.id)
        if not user:
            return ServiceResult(AuthException.WrongToken())
        return ServiceResult(user)
