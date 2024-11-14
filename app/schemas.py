from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class BasePost(BaseModel):
    title: str
    content: str
    published: bool = True


class CreatePost(BasePost):
    pass


class UpdatePost(BasePost):
    pass


class PostResponse(BasePost):
    id: int
    created_at: datetime


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_id: Optional[str] = None
