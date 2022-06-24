from sqlalchemy import (Column, Integer, String, Table, ForeignKey)

from app.db.db import Base


class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    content = Column(String)

