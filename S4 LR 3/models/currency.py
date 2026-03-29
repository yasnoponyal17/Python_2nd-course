from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, relationship
from models.user import User
from models.subscription import Subscription
from models.base import Base

class Currency(Base):
    __tablename__ = "currencies"
    id = Column(Integer, primary_key=True)
    code = Column(String, unique=True)
    name = Column(String)
    
    users = relationship("User", secondary="subscriptions", back_populates="currencies")