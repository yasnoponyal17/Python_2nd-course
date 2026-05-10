import httpx

from lxml import etree
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db

from models import Currency
from schemas import CurrencyResponse

router = APIRouter(prefix='/currencies', tags=['currencies'])

@router.get('/', response_model=list[CurrencyResponse])
async def get_currencies(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Currency))
    currencies = result.scalars().all()
    return currencies

@router.post('/update')
async def update_currencies(db: AsyncSession = Depends(get_db)):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://www.cbr.ru/scripts/XML_daily.asp")
    root = etree.fromstring(response.content)
    for valute in root.findall('Valute'):
        code = valute.find('CharCode').text
        name = valute.find('Name').text
        value = valute.find('Value').text

        result = await db.execute(select(Currency).where(Currency.code == code))
        currency = result.scalar_one_or_none()

        if currency is None:
            currency = Currency(code=code, name=name, rate=float(value.replace(',', '.')))
            db.add(currency)
        else:
            currency.name = name
            currency.rate = float(value.replace(',', '.'))

    await db.commit()
    return {"detail": "Валюты успешно обновлены"}

@router.get('/{currency_code}/rate', response_model=CurrencyResponse)
async def get_currency(currency_code: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Currency).where(Currency.code == currency_code))
    currency = result.scalar_one_or_none()
    if currency is None:
        raise HTTPException(status_code=404, detail="Валюта с таким кодом не найдена")
    return currency