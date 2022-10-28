from typing import List
from pydantic import BaseModel, validator, Field
from datetime import date


class Genre(BaseModel):
    name: str


class Book(BaseModel):
    title: str
    writer: str
    duration: str
    date: date
    summary: str = None
    genres: List[Genre]
    pages: int


class Author(BaseModel):
    first_name: str = Field(..., min_length=10, description='имя не более 10')
    last_name: str
    age: int = Field(..., gt=15, lt=90, description='возаст не более 90')

    # @validator('age')
    # def check_value(cls, v):
    #     if v < 15:
    #         raise ValueError('возраст не меньше 15')
    #     return v


class BookOut(Book):
    id: int


