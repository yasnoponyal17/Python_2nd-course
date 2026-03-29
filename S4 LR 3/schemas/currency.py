from pydantic import BaseModel

class CurrencyResponse(BaseModel):
    id: int
    code: str
    name: str

    class Config:
        orm_mode = True