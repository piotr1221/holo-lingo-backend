from typing import Union
from pydantic import BaseModel


class ClassicUserPost(BaseModel):
    name: str
    password: str
    email: str

class ModifyUserPost(BaseModel):
    id: str
    name: str