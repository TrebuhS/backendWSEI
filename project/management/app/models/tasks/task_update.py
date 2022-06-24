from typing import List

from pydantic import BaseModel

from app.models.categories.category_details import Category


class TaskUpdate(BaseModel):
    id: int
    content: str
    is_done: bool
    category_id: int
    tags_ids: List[int]
