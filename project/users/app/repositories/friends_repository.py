from app.db.tables.friends import user_friends
from app.models.users.user_create import UserCreate
from app.shared.base_crud import BaseCRUD
from app.db.tables.user import User


class FriendsRepository(BaseCRUD):

    def add_friendship(self, friend_one_id: int, friend_two_id: int):
        friend_one: User = self._db.query(User).filter(User.id == friend_one_id).first()
        friend_two: User = self._db.query(User).filter(User.id == friend_two_id).first()
        friend_one.friends.append(friend_two)
        found_friends = self._db.query(user_friends).all()
        self._db.add_all([friend_one, friend_two])
        self._db.commit()
