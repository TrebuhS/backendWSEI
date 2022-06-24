from typing import Union

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from pydantic.validators import timedelta, datetime
from sqlalchemy.orm import Session
from starlette.requests import Request

from app.db.db import get_db
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
        self.__users_repository = users_repository
        self.__oauth = oauth
        self.__crypt_helper = crypt_helper

    def login(self, form_data: OAuth2PasswordRequestForm) -> ServiceResult:
        user = self.__authenticate_user(form_data.username, form_data.password)
        if not user:
            return ServiceResult(AuthException.IncorrectCredentials())
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = self.__create_access_token(
            data={"sub": str(user.id)},
            expires_delta=access_token_expires
        )
        return ServiceResult({
            "access_token": access_token,
            "token_type": "bearer"
        })

    def handle_token_verification(self, request: Request) -> ServiceResult:
        token = request.headers.get("Authorization")
        if not token:
            return ServiceResult(AuthException.WrongToken())
        token = token.split()[1]
        return self.__get_current_user(token)

    def __get_current_user(self, token: str):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            user_id: int = payload.get("sub")
            if not user_id:
                return ServiceResult(AuthException.WrongToken())
            token_data = TokenData(id=user_id)
        except JWTError:
            return ServiceResult(AuthException.WrongToken())
        user = self.__users_repository.get_user(token_data.id)
        if not user:
            return ServiceResult(AuthException.WrongToken())
        return ServiceResult(user)

    def __authenticate_user(self, username: str, password: str):
        user = self.__users_repository.get_user_by_email(username)
        if not user:
            return None
        if not self.__crypt_helper.verify_password(password, user.password):
            return None
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
