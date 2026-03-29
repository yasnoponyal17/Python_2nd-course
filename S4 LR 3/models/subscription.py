from sqlalchemy import Column, ForeignKey, UniqueConstraint
from models.base import Base

class Subscription(Base):
    __tablename__ = "subscriptions"
    user_id = Column(ForeignKey("users.id"), primary_key=True)
    currency_id = Column(ForeignKey("currencies.id"), primary_key=True)
    
    __table_args__ = (UniqueConstraint("user_id", "currency_id"), )
    