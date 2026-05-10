from pydantic import BaseModel, EmailStr
from schemas.currency import CurrencyResponse
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: EmailStr

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    currencies: list[CurrencyResponse] = []

    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None