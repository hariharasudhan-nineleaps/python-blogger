from typing import TypeVar, Generic
from pydantic import generics, BaseModel
from pydantic.generics import GenericModel


T = TypeVar("T")
M = TypeVar("M")


class APIResponse(GenericModel, Generic[T, M]):
    data: T
    metadata: M

    class Config:
        extra = 'ignore'


class GenerateTokenRequestBody(BaseModel):
    id: str
    name: str
    username: str
    email: str

    class Config:
        extra = 'ignore'


class GenerateTokenResponse(BaseModel):
    access_token: str

    class Config:
        extra = 'ignore'


class ExchangeTokenResponse(BaseModel):
    access_token: str

    class Config:
        extra = 'ignore'