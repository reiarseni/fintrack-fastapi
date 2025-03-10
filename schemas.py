from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime
from models import TransactionType

# User schemas
class UserBase(BaseModel):
    email: EmailStr
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

# Category schemas
class CategoryBase(BaseModel):
    name: str
    type: TransactionType

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

# Transaction schemas
class TransactionBase(BaseModel):
    amount: float
    description: str
    type: TransactionType
    category_id: int

class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase):
    id: int
    date: datetime
    owner_id: int

    class Config:
        orm_mode = True

# Token schemas
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
