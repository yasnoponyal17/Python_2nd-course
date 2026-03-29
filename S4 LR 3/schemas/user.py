from pydantic import BaseModel, ConfigDict
from typing import List

class UserCreate(BaseModel):
    username: str
    email: str
    
class UserUpdate(BaseModel):
    username: str
    email: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    currencies: List[str] = []

    model_config = ConfigDict(from_attributes=True)