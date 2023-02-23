from typing import Optional, Generic, TypeVar
from pydantic import BaseModel, constr, conint
from pydantic.generics import GenericModel

T = TypeVar('T')


class UserSchema(BaseModel):
    name: constr(min_length=1, max_length=100, strict=True)
    age: conint(ge=0, le=100, strict=True)

    class Config:
        orm_mode = True


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
