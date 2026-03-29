from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from database import get_session
from models.user import User
from models.currency import Currency
from models.subscription import Subscription
from schemas.subscription import SubscriptionRequest

router = APIRouter(prefix="/subscriptions", tags=["Subscriptions"])

@router.post("/", status_code=status.HTTP_201_CREATED)
async def subscribe(req: SubscriptionRequest, db: AsyncSession = Depends(get_session)):
    user_result = await db.execute(select(User).where(User.id == req.user_id))
    user = user_result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    curr_result = await db.execute(select(Currency).where(Currency.code == req.currency_code.upper()))
    currency = curr_result.scalar_one_or_none()
    if not currency:
        raise HTTPException(status_code=404, detail="Currency not found. Update currencies first.")

    sub_query = select(Subscription).where(
        Subscription.user_id == user.id,
        Subscription.currency_id == currency.id
    )
    existing_sub = (await db.execute(sub_query)).scalar_one_or_none()
    if existing_sub:
        raise HTTPException(status_code=409, detail="Subscription already exists")

    new_sub = Subscription(user_id=user.id, currency_id=currency.id)
    db.add(new_sub)
    await db.commit()
    
    return {"message": f"User {user.username} subscribed to {currency.code}"}

@router.delete("/")
async def unsubscribe(req: SubscriptionRequest, db: AsyncSession = Depends(get_session)):
    curr_result = await db.execute(select(Currency).where(Currency.code == req.currency_code.upper()))
    currency = curr_result.scalar_one_or_none()
    
    if not currency:
        raise HTTPException(status_code=404, detail="Currency not found")

    sub_query = select(Subscription).where(
        Subscription.user_id == req.user_id,
        Subscription.currency_id == currency.id
    )
    sub_result = await db.execute(sub_query)
    subscription = sub_result.scalar_one_or_none()

    if not subscription:
        raise HTTPException(status_code=404, detail="Subscription not found")

    await db.delete(subscription)
    await db.commit()
    
    return {"message": "Successfully unsubscribed"}