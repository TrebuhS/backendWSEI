from sqlalchemy.orm import joinedload, subqueryload

from app.db.tables.friends import user_friends
from app.models.users.user_create import UserCreate
from app.shared.base_crud import BaseCRUD
from app.db.tables.user import User


class UsersRepository(BaseCRUD):

    def add_user(self, user: UserCreate):
        new_user = User(
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            password=user.password
        )
        self._db.add(new_user)
        self._db.commit()
        self._db.refresh(new_user)
        return new_user

    def get_user(self, user_id: int):
        user = self._db.query(User)\
            .filter(User.id == user_id)\
            .first()
        return user

    def get_user_by_email(self, email: str):
        return self._db.query(User).filter(User.email == email).first()
