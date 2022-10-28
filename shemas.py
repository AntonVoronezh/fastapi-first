from typing import List
from pydantic import BaseModel
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


