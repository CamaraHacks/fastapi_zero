from fastapi import FastAPI
from http import HTTPStatus
from fastapi.responses import HTMLResponse
app = FastAPI()

from fastapi_zero.schemas import Message

@app.get('/', 
         status_code=HTTPStatus.OK,
         response_model=Message
         )
def read_root():
    return {'message': 'Ola mundo!'}

@app.get('/index',
         response_class=HTMLResponse
         )

def index():
    return """
    <html>
      <head>
        <title>Nosso olá mundo!</title>
      </head>
      <body>
        <h1> Olá Mundo </h1>
      </body>
    </html>"""
