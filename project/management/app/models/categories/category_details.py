from typing import List

from pydantic import BaseModel


class Category(BaseModel):
    id: int
    name: str
    tasks: List[int]

    class Config:
        orm_mode = True
