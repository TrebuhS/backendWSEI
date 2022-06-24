from sqlalchemy.orm import relationship

from app.db.tables.category import Category
from app.db.tables.note import Note
from app.db.tables.note_tag import note_tag
from app.db.tables.tag import Tag
from app.db.tables.task import Task
from app.db.tables.task_tag import task_tag

Category.tasks = relationship(Task, back_populates="category")
Note.tags = relationship(Tag, secondary=note_tag, back_populates="notes")
Tag.tasks = relationship(Task, secondary=task_tag, back_populates="tags")
Tag.notes = relationship(Note, secondary=note_tag, back_populates="tags")
Task.category = relationship(Category, back_populates="tasks")
Task.tags = relationship(Tag, secondary=task_tag, back_populates="tasks")
