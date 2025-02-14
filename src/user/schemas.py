from pydantic import BaseModel, EmailStr
from typing import Optional
import datetime


class UserBase(BaseModel):
    username: str
    email: EmailStr
    name: Optional[str] = None


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: int
    created_at: datetime.datetime
    balance: float

    class Config:
        from_attributes = True
