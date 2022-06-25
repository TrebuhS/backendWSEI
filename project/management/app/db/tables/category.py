from sqlalchemy import (Table, Column, Integer, String, ForeignKey, UniqueConstraint)
from sqlalchemy.orm import relationship

from app.db.db import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    name = Column(String)

    tasks = relationship("Task", back_populates="category")