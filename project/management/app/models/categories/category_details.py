from typing import List

from pydantic import BaseModel

from app.models.tasks.task_details import Task


class Category(BaseModel):
    id: int
    name: str
    tasks: List[Task]

    class Config:
        orm_mode = True
