from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, ForeignKey
from database import Base

class Subscription(Base):
    __tablename__ = 'subscriptions'

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'), primary_key=True)
    currency_id: Mapped[int] = mapped_column(Integer, ForeignKey('currencies.id'), primary_key=True)