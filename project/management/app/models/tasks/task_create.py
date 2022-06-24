from pydantic import BaseModel


class TaskCreate(BaseModel):
    content: str