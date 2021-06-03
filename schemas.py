
from pydantic import BaseModel
from sqlalchemy import orm
from typing import List, Optional


class BlogBase(BaseModel):
    title: str
    body: str
    user_id: int


class Blog(BlogBase):
    class Config():
        orm_mode = True


class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List

    class Config():
        orm_mode = True


class ShowBlog(BaseModel):
    title: str
    body: str
    user_id: int
    creator: ShowUser

    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
    scopes: List[str] = []
