from typing import Union
from pydantic import BaseModel


class UserPost(BaseModel):
    name: str
    password: str

class UserName(BaseModel):
    name: str