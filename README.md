# fast_zero
Curso de FastApi

Cria e ativa o ambiente virtual:
`poetry shell`   

Sobe a app `fastapi dev fast_zero/app.py` ou `task run`

Sobe um servidor e disponibiliza na rede local
`fastapi dev fast_zero/app.py --host 0.0.0.0`  

Formata código `task format`

Migrations
`alembic init migrations`
`alembic revision --autogenerate -m "create todos table"`
`alembic upgrade head`

Rodar teste e pausar no erro e debugar
`task test -x --pdb`
