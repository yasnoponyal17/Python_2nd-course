from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer
from database import Base

class Currency(Base):
    __tablename__ = 'currencies'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    code: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    rate: Mapped[float] = mapped_column(nullable=True)