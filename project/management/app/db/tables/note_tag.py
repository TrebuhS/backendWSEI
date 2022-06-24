from sqlalchemy import ForeignKey, Column, Table

from app.db.db import Base

note_tag = Table(
    "note_tag",
    Base.metadata,
    Column("note_id", ForeignKey("notes.id")),
    Column("tag_id", ForeignKey("tags.id"))
)
