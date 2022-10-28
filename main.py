from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def home():
    return {'key': 'hello'}


@app.get('/{pk}')
def get_item(pk: int, q: str = None): # http://127.0.0.1:8000/7777?q=iouo
    return {'key': pk, 'q': q}

