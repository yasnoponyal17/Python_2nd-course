from pydantic import BaseModel

class SubscriptionRequest(BaseModel):
    user_id: int
    currency_id: int