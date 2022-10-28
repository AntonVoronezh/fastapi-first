# uvicorn main:app --reload
from fastapi import FastAPI

from shemas import Book

app = FastAPI()


@app.get('/')
def home():
    return {'key': 'hello'}


@app.get('/{pk}')
def get_item(pk: int, q: str = None):  # http://127.0.0.1:8000/7777?q=iouo
    return {'key': pk, 'q': q}


@app.get('/users/{pk}/items/{item}')  # http://127.0.0.1:8000/users/2/items/tttgr
def get_user_item(pk: int, item: str):
    return {'pk': pk, 'item': item}


@app.post('/book')
def create_book(book: Book):
    return book
