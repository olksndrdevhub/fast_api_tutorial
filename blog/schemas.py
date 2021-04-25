from typing import List
from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str
    password: str


class Blog(BaseModel):
    title:str
    body:str

    orm_mode = True



# schema for responce
class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List

    class Config:
        orm_mode = True

# schema for responce
class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser

    class Config:
        orm_mode = True



