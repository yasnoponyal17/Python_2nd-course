from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from models.base import Base
import models.user
import models.currency
import models.subscription

DATABASE_URL = "sqlite+aiosqlite:///./app.db"

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session

async def init_db():
	async with engine.begin() as conn:
		await conn.run_sync(Base.metadata.create_all)
