from typing import List

from pydantic import BaseModel

from app.models.categories.category_details import Category
from app.models.tags.tag_details import Tag


class Task(BaseModel):
    id: int
    content: str
    is_done: bool
    category: Category
    tags: List[Tag]

    class Config:
        orm_mode = True
