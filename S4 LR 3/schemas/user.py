from pydantic import BaseModel
from typing import List

class UserCreate(BaseModel):
    username: str
    email: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    currencies: List[str] = []

    class Config:
        orm_mode = True