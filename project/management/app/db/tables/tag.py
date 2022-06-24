from sqlalchemy import (Column, Integer, String)
from sqlalchemy.orm import relationship

from app.db.db import Base
from app.db.tables.note_tag import note_tag
from app.db.tables.task_tag import task_tag


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    name = Column(String)

    tasks = relationship("Task", secondary=task_tag, back_populates="tags")
    notes = relationship("Note", secondary=note_tag, back_populates="tags")
