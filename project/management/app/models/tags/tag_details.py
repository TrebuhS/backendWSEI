from typing import List

from pydantic import BaseModel

from app.models.notes.note_details import Note
from app.models.tasks.task_details import Task


class Tag(BaseModel):
    id: int
    name: str
    tasks: List[Task]
    notes: List[Note]

    class Config:
        orm_mode = True
