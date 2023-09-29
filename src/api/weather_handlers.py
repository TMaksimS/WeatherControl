from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_db
from settings import LOGER

app = APIRouter(prefix="/weather", tags=["weather"])


@app.post("", response_model="")
@LOGER.catch
async def get_uniq_weather_by_name():
    pass


@LOGER.catch()
@app.get("", response_model="")
async def get_weather_my_cities(session: AsyncSession = Depends(get_db)):
    pass
