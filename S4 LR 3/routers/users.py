from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from typing import List

from models.user import User
from schemas.user import UserCreate, UserResponse, UserUpdate
from database import get_session

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, session: AsyncSession = Depends(get_session)):
    existing_query = await session.execute(
        select(User).where((User.username == user.username) | (User.email == user.email))
    )
    if existing_query.scalars().first():
        raise HTTPException(status_code=400, detail="User with this username/email already exists")

    db_user = User(username=user.username, email=user.email)
    session.add(db_user)
    await session.commit()
    await session.refresh(db_user)
    return db_user

@router.get("/", response_model=List[UserResponse])
async def get_users(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(User).options(selectinload(User.currencies)))
    return result.scalars().all()

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, session: AsyncSession = Depends(get_session)):
    result = await session.execute(
        select(User).options(selectinload(User.currencies)).where(User.id == user_id)
    )
    db_user = result.scalar_one_or_none()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.put("/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user_update: UserUpdate, session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(User).where(User.id == user_id))
    db_user = result.scalar_one_or_none()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db_user.email = user_update.email
    await session.commit()
    await session.refresh(db_user)
    return db_user

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int, session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(User).where(User.id == user_id))
    db_user = result.scalar_one_or_none()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    await session.delete(db_user)
    await session.commit()
    return None