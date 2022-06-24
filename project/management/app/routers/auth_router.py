from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session
from starlette.requests import Request

from app.repositories.categories_repository import UsersRepository
from app.services.auth.auth_service import AuthService
from app.db.db import get_db
from app.shared.app_request import AppRequest
from app.shared.helpers.crypt_helper import CryptHelper
from app.shared.service_result import handle_result

router = APIRouter()

def get_auth_service(db: Session = Depends(get_db)):
    return AuthService(
        db,
        UsersRepository(db),
        OAuth2PasswordBearer("/login"),
        CryptHelper()
    )


@cbv(router)
class UsersRouter:

    __db: Session = Depends(get_db)
    __service: AuthService = Depends(get_auth_service)

    @router.get("/")
    async def verify_token(
            self,
            request: Request
    ):
        result = self.__service.handle_token_verification(request)
        return handle_result(result)

    @router.post("/login")
    async def login_for_access_token(
            self,
            form_data: OAuth2PasswordRequestForm = Depends()
    ):
        result = self.__service.login(form_data)
        return handle_result(result)
