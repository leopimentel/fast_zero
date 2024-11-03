from pydantic import BaseModel, ConfigDict, EmailStr


class BatataFritaModel(BaseModel):
    message: str
    batata: str


# Código omitido


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    username: str
    email: EmailStr
    id: int
    model_config = ConfigDict(from_attributes=True)


class UserDB(UserSchema):
    id: int


class Message(BaseModel):
    message: str


class UserList(BaseModel):
    users: list[UserPublic]
