from pydantic import BaseModel


class BatataFritaModel(BaseModel):
    message: str
    batata: str
