from typing import TypeVar, Generic

from pydantic.generics import GenericModel
from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime


T = TypeVar("T")
M = TypeVar("M")


class SignupRequestBody(BaseModel):
    name: Optional[str] = Field(default=None, max_length=100)
    email: EmailStr
    password: str = Field(max_length=100)
    username: str = Field(max_length=20)

    class Config:
        extra = 'forbid'


class LoginRequstBody(BaseModel):
    email: EmailStr
    password: str = Field(max_length=100)

    class Config:
        extra = 'forbid'


class APIResponse(GenericModel, Generic[T, M]):
    data: T
    metadata: M

    class Config:
        extra = 'forbid'


class SignUpResponse(BaseModel):
    id: str
    name: str
    email: str
    username: str
    created_at: datetime

    class Config:
        extra = 'ignore'
        orm_mode = True


class TokenData(BaseModel):
    id: str
    name: str
    username: str
    email: str

    class Config:
        extra = 'ignore'

    @property
    def user_id(self):
        return self.id