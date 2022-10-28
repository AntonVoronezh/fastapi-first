# uvicorn main:app --reload
from fastapi import FastAPI, Query, Path, Body

from shemas import Book, Author, BookOut

app = FastAPI()


@app.get('/')
def home():
    return {'key': 'hello'}


@app.get('/1/{pk}')
def get_item(pk: int, q: str = None):  # http://127.0.0.1:8000/1/7777?q=iouo
    return {'key': pk, 'q': q}


@app.get('/users/{pk}/items/{item}')  # http://127.0.0.1:8000/users/2/items/tttgr
def get_user_item(pk: int, item: str):
    return {'pk': pk, 'item': item}


@app.post('/book')
def create_book(item: Book, author: Author, quantity: int = Body(...)):  # без Body попадет в запрос
    return {'item': item, 'author': author, 'quantity': quantity}


@app.get('/book')  # http://127.0.0.1:8000/book?q=hhhh
def get_book(q: str = Query(None, max_length=5, min_length=2, description='Это то-то и то-то')):
    # def get_book(q: str = Query(..., max_length=5) - обязательный параметр ...
    # def get_book(q: str = Query("test", max_length=5) - параметр по умолчанию
    # def get_book(q: List[str] = ) - лист значений
    # def get_book(q: List[str] = Query(["test", "test2"]) - лист значений с параметр по умолчанию
    # def get_book(q: str = Query(..., , deprecated=True) - устаревший параметр
    return q


@app.get('book/{pk}')
def get_single_book(pk: int = Path(..., qt=1, le=20),
                    pages: int = Query(None, qt=10, le=500)):  # значение больше 1 и менбше 20
    return {'pk': pk, 'pages': pages}


@app.post('/author', name='yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy')
def create_author(author: Author = Body(..., embed=True)):  # сразу вложенность
    return {'author': author}


@app.post('/book2', response_model=BookOut, response_model_exclude={'date'})
# response_model_exclude - исключить что-то из ответа
def create_book2(item: Book):
    # book = item.dict()
    # book['id'] = 11111111111
    # return book
    return BookOut(**item.dict(), id=4444444)
