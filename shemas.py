from typing import List
from pydantic import BaseModel, validator
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
    first_name: str
    last_name: str
    age: int

    @validator('age')
    def check_value(cls, v):
        if v < 15:
            raise ValueError('возраст не меньше 15')
        return v


