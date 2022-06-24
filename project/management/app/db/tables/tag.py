from sqlalchemy import (Column, Integer, String)
from sqlalchemy.orm import relationship

from app.db.db import Base


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    name = Column(String)
