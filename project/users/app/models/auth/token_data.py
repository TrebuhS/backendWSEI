from typing import Union

from pydantic import BaseModel


class TokenData(BaseModel):
    id: Union[int, None] = None
