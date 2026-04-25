from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional, Literal
class PostBase(BaseModel):
    name: str
    author: str
    rating: Optional[int] = None
    year_published: int

class PostCreate(PostBase):
    pass


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True

class Post(BaseModel):
    name: str
    author: str
    year_published: int
    posted_at: datetime
    owner_id: int
    owner: UserOut
    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    email:EmailStr
    password: str





class UserLogin(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token :str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] =None
 

class Vote(BaseModel):
    post_id: int
    dir: Literal[0,1]