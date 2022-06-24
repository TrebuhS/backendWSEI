from sqlalchemy import ForeignKey, Column, Table

from app.db.db import Base

task_tag = Table(
    "task_tag",
    Base.metadata,
    Column("task_id", ForeignKey("tasks.id")),
    Column("tag_id", ForeignKey("tags.id"))
)
