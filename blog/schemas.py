from os import name
from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    body: str

class ShowBlog(BaseModel):
    title: str
    class Comfig():
        orm_mode = True
class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str

    class Comfig():
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str
