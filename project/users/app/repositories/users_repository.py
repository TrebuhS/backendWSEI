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
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    def get_user(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()

    def get_user_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()
