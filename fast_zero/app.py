from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.routers import auth, users
from fast_zero.schemas import (
    BatataFritaModel,
)

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)


@app.get('/')
def read_root():
    return {'message': 'Olá Mundo!'}


@app.get('/getjson', response_model=BatataFritaModel)
def read_root2():
    return {'message': 'Olá Mundo!', 'batata': 'frita'}


@app.get('/gethtml', response_class=HTMLResponse)
def read_root3():
    return """
    <html>
      <head>
        <title> Nosso olá mundo!</title>
      </head>
      <body>
        <h1> Olá Mundo </h1>
      </body>
    </html>
"""
