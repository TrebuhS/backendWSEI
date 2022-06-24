from sqlalchemy import (Column, Integer, String, Boolean, ForeignKey, Table)
from sqlalchemy.orm import relationship

from app.db.db import Base
from app.db.tables import task_tag


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    content = Column(String)
    is_done = Column(Boolean, default=False)

    category_id = Column(Integer, ForeignKey("categories.id"))
