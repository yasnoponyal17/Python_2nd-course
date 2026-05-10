from pydantic import BaseModel

class CurrencyResponse(BaseModel):
    id: int
    code: str
    name: str
    rate: float | None

    class Config:
        from_attributes = True