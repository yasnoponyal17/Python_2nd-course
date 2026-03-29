import httpx
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from database import get_session
from models.currency import Currency

router = APIRouter(prefix="/currencies", tags=["Currencies"])

JSON_URL = "https://www.cbr-xml-daily.ru/daily_json.js"

@router.post("/update")
async def update_currencies(db: AsyncSession = Depends(get_session)):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(JSON_URL)
            response.raise_for_status()
            data = response.json()
        except Exception:
            raise HTTPException(status_code=502, detail="Не удалось получить данные от ЦБ")

    valutes = data.get('Valute', {})
    
    for code, info in valutes.items():
        stmt = select(Currency).where(Currency.code == code)
        result = await db.execute(stmt)
        currency_obj = result.scalar_one_or_none()

        if currency_obj:
            currency_obj.name = info['Name']
        else:
            new_curr = Currency(code=code, name=info['Name'])
            db.add(new_curr)

    await db.commit()
    return {"status": "success", "message": f"Updated {len(valutes)} currencies"}

@router.get("/{currency_code}/rate")
async def get_rate(currency_code: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(JSON_URL)
        data = response.json()
    
    valutes = data.get('Valute', {})
    upper_code = currency_code.upper()

    if upper_code not in valutes:
        raise HTTPException(status_code=404, detail="Валюта не найдена в данных ЦБ")
    
    valute_data = valutes[upper_code]
    return {
        "code": upper_code,
        "name": valute_data['Name'],
        "rate": valute_data['Value'],
        "nominal": valute_data['Nominal']
    }