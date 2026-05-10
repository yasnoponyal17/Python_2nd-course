from pydantic import BaseModel

class SubscriptionCreate(BaseModel):
    user_id: int
    currency_id: int

class SubscriptionResponse(BaseModel):
    user_id: int
    currency_id: int

    class Config:
        from_attributes = True