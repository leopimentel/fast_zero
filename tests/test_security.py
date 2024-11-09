from http import HTTPStatus

import pytest
from fastapi import HTTPException
from jwt import decode

from fast_zero.security import (
    create_access_token,
    get_current_user,
)
from fast_zero.settings import Settings

settings = Settings()


def test_jwt(session):
    data = {'test': 'test'}
    token = create_access_token(data)

    decoded = decode(token, settings.SECRET_KEY, algorithms=['HS256'])

    assert decoded['test'] == data['test']
    assert decoded['exp']  # Testa se o valor de exp foi adicionado ao token

    with pytest.raises(HTTPException):
        get_current_user(session, token)


def test_jwt_invalid_token(client):
    response = client.delete(
        '/users/1', headers={'Authorization': 'Bearer token-invalido'}
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}


def test_jwt_user_not_in_db(session):
    data = {'test': 'test', 'sub': 'email@email.com'}
    token = create_access_token(data)

    decoded = decode(token, settings.SECRET_KEY, algorithms=['HS256'])

    assert decoded['test'] == data['test']
    assert decoded['exp']  # Testa se o valor de exp foi adicionado ao token

    with pytest.raises(HTTPException):
        get_current_user(session, token)
