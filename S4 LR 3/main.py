from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import init_db
from routers.users import router as user_router
from routers.currencies import router as currency_router
from routers.subscriptions import router as subscription_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(user_router)
app.include_router(currency_router)
app.include_router(subscription_router)

@app.get("/")
async def root():
    return {"message": "Currency Tracker API is running"}