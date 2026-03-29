from pydantic import BaseModel

class SubscriptionCreate(BaseModel):
    user_id: int
    currency_id: int