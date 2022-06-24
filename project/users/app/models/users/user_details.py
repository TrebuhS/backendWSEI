from typing import List

from pydantic import BaseModel


class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    password: str
    friends: List[int]

    class Config:
        orm_mode = True
