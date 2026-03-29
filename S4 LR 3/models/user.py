from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import DeclarativeBase, relationship
import datetime
from models.currency import Currency
from models.subscription import Subscription

class Base(DeclarativeBase): pass

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    
    currencies = relationship("Currency", secondary="subscriptions", back_populates="users")
    