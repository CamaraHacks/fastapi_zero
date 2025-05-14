from fastapi.testclient import TestClient
from http import HTTPStatus

from fastapi_zero.app import app


def test_root_deve_retornar_ola_mundo():
    client = TestClient(app) #Arrange

    response = client.get('/') #Act

    assert response.status_code == HTTPStatus.OK #Assert
    assert response.json() == {'message': 'Ola mundo!'} #Assert


def teste_index():
    client = TestClient(app) #Arrange

    response = client.get('/index') #act

    assert response.status_code == HTTPStatus.OK #Assert
    assert <h1>Olá mundo </h1> in response.text


