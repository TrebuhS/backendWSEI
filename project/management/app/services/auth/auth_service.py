from starlette.requests import Request

from app.services.auth.auth_exception import AuthException
from app.shared.base_service import BaseService
from app.shared.service_result import ServiceResult

class AuthService(BaseService):

    def handle_token_verification(self, request: Request) -> ServiceResult:
        token = request.headers.get("Authorization")
        if not token:
            return ServiceResult(AuthException.WrongToken())
        token = token.split()[1]
        return self.__get_current_user(token)

    def __get_current_user(self, token: str):
        return 1
