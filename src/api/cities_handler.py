import json

from fastapi import APIRouter, Depends, Response
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_db
from src.database.crud import CityDB, WeatherDB
from settings import LOGER
from src.database.schemas import CreateData, GetAllInfo, GetAllData


app = APIRouter(prefix="/cities", tags=["cities"])


@app.get("/", response_model=GetAllData)
@LOGER.catch
async def get_my_cities(session: AsyncSession = Depends(get_db)):
    data = CityDB(session=session)
    result = await data.get_all_cities_with_weather()
    new = [GetAllInfo.model_validate(i) for i in result]
    return new


@app.post("/", response_model="")
@LOGER.catch
async def add_city(body: CreateData, session: AsyncSession = Depends(get_db)):
    data = CityDB(session=session)
    await data.add_city(dict(body))
    print(data)
    return None


@app.delete("/", response_model="")
@LOGER.catch
async def delete_city(session: AsyncSession = Depends(get_db)):
    pass


@app.post("/wet")
@LOGER.catch
async def add_weather(data: dict, session: AsyncSession = Depends(get_db)):
    step = CityDB(session=session)
    await step.add_weather(data=data)
    return None
