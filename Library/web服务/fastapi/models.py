"""
@Author: Jonescyna@gmail.com
@Created: 2021/3/9
"""
from pydantic import BaseModel, Field


class LoginByPhone(BaseModel):
    phone: str
    code: int


class LoginByUsername(BaseModel):
    username: str
    password: str
    is_save: bool = False
