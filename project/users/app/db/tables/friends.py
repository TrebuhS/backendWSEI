from sqlalchemy import (Table, Column, Integer, String, ForeignKey, UniqueConstraint)
from sqlalchemy.orm import relationship

from app.db.db import Base


user_friends = Table(
    'friends',
    Base.metadata,
    Column('friend_a_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('friend_b_id', Integer, ForeignKey('users.id'), primary_key=True),
    UniqueConstraint('friend_a_id', 'friend_b_id'),
)
