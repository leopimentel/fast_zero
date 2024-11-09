from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_root2_deve_retornar_json(client):
    response = client.get('/getjson')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!', 'batata': 'frita'}


def test_root3_deve_retornar_html(client):
    response = client.get('/gethtml')

    assert response.status_code == HTTPStatus.OK
    assert (
        response.text
        == """
    <html>
      <head>
        <title> Nosso olá mundo!</title>
      </head>
      <body>
        <h1> Olá Mundo </h1>
      </body>
    </html>
"""
    )
