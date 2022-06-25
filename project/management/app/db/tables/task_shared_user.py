from sqlalchemy import ForeignKey, Column, Table, Integer
from sqlalchemy.orm import relationship

from app.db.db import Base


class TaskSharedUser(Base):
    __tablename__ = "tasks_shared_users"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    task_id = Column(Integer, ForeignKey("tasks.id"))

    task = relationship("Task", back_populates="shared")