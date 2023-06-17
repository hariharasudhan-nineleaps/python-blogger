from typing import TypeVar, Generic, Union
from pydantic.generics import GenericModel

T = TypeVar("T")
M = TypeVar("M")

class APIResponse(GenericModel, Generic[T, M]):
    metadata: M
    data: T

    class Config:
        extra = 'forbid'
