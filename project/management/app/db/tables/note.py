from sqlalchemy import (Column, Integer, String, Table, ForeignKey)
from sqlalchemy.orm import relationship

from app.db.db import Base
from app.db.tables.note_tag import note_tag


class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    content = Column(String)

    tags = relationship("Tag", secondary=note_tag, back_populates="notes", lazy="joined")
