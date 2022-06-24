from sqlalchemy import (Table, Column, Integer, String, select)
from sqlalchemy.orm import relationship

from app.db.tables.friends import user_friends
from app.db.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

    friends = relationship(
        "User",
        secondary=user_friends,
        primaryjoin=id == user_friends.c.friend_a_id,
        secondaryjoin=id == user_friends.c.friend_b_id,
    )
