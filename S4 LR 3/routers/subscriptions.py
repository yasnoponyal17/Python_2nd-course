from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from database import get_db

from models import Subscription
from schemas import SubscriptionCreate, SubscriptionResponse

router = APIRouter(prefix='/subscriptions', tags=['subscriptions'])

@router.post('/', response_model=SubscriptionResponse)
async def create_subscription(sub_data: SubscriptionCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Subscription).where(Subscription.user_id == sub_data.user_id, Subscription.currency_id == sub_data.currency_id))
    subscription = result.scalar_one_or_none()
    if subscription:
        raise HTTPException(status_code=409, detail="Подписка уже существует")
    
    new_subscription = Subscription(user_id = sub_data.user_id, currency_id = sub_data.currency_id)
    db.add(new_subscription)
    try:
        await db.commit()
        await db.refresh(new_subscription)
        return new_subscription
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=409, detail="Подписка уже существует")


@router.delete('/')
async def delete_subscription(sub_data: SubscriptionCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Subscription).where(Subscription.user_id == sub_data.user_id, Subscription.currency_id == sub_data.currency_id))
    subscription = result.scalar_one_or_none()
    if subscription is None:
        raise HTTPException(status_code=404, detail='Подписка не найдена')
    await db.delete(subscription)
    await db.commit()
    return {"detail": "Подписка успешно удалена"}