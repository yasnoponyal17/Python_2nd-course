from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from database import get_db

from models import User, Currency, Subscription
from schemas import UserCreate, UserResponse, UserUpdate

router = APIRouter(prefix='/users', tags=["users"])

@router.get('/', response_model=list[UserResponse])
async def get_users(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User))
    users = result.scalars().all()
    return users

@router.post('/', response_model=UserResponse)
async def create_user(user_data: UserCreate, db: AsyncSession = Depends(get_db)):
    new_user = User(username=user_data.username, email=user_data.email)
    db.add(new_user)
    try:
        await db.commit()
        await db.refresh(new_user)
        return new_user
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=409, detail="Пользователь с таким именем или email уже существует.")

@router.get('/{user_id}', response_model=UserResponse)
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await db.get(User, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Пользователь с таким id не найден")
    result = await db.execute(select(Currency).join(Subscription, Subscription.currency_id == Currency.id).where(Subscription.user_id == user_id))
    currencies = result.scalars().all()
    
    return {"id": user.id, "username": user.username, "email": user.email, "currencies": currencies}

@router.put('/{user_id}', response_model=UserResponse)
async def put_user(user_data: UserUpdate, user_id: int, db: AsyncSession = Depends(get_db)):
    user = await db.get(User, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Пользователь с таким id не найден")
    user.email = user_data.email
    await db.commit()
    await db.refresh(user)
    return user

@router.delete('/{user_id}')
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await db.get(User, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Пользователь с таким id не найден")
    await db.delete(user)
    await db.commit()
    return {"detail": "Пользователь успешно удален."}