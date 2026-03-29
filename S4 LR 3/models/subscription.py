from sqlalchemy import Column, ForeignKey, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, relationship
from models.user import User
from models.currency import Currency
from models.base import Base

class Subscription(Base):
    __tablename__ = "subscriptions"
    user_id = Column(ForeignKey("users.id"), primary_key=True)
    currency_id = Column(ForeignKey("currencies.id"), primary_key=True)
    
    __table_args__ = (UniqueConstraint("user_id", "currency_id"))
    
    user = relationship("User", back_populates="subscriptions")
    currency = relationship("Currency", back_populates="subscriptions")