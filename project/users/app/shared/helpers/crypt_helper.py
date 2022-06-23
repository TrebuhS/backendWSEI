from passlib.context import CryptContext


class CryptHelper:
    __pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def verify_password(self, plain_password, hashed_password):
        return self.__pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password):
        return self.__pwd_context.hash(password)
