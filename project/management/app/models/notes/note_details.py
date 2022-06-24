from typing import List

from pydantic import BaseModel

from app.models.tags.tag_details import Tag


class Note(BaseModel):
    id: int
    content: str
    tags: List[Tag]

    class Config:
        orm_mode = True
