from typing import List

from pydantic import BaseModel


class NoteUpdate(BaseModel):
    id: int
    content: str
    tags: List[int]
