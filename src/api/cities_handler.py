from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import JSONResponse

from src.database import get_db
from src.database.crud import CityDB
from settings import LOGER
from src.database.schemas import CreateData, GetAllInfo, GetAllData


app = APIRouter(prefix="/cities", tags=["cities"])


@app.get("")
@LOGER.catch
async def get_my_cities(session: AsyncSession = Depends(get_db)):
    """Эндпоинт возвращает все города с их погодными данными из БД"""
    data = CityDB(session=session)
    result = await data.get_all_cities_with_weather()
    new = [GetAllInfo.model_validate(i) for i in result]
    try:
        new[0]
    except IndexError:
        return HTTPException(status_code=404, detail="Empty result")
    return GetAllData(data=new)


@app.post("")
@LOGER.catch
async def add_city(body: CreateData, session: AsyncSession = Depends(get_db)):
    """Эндпоинт добавляет город в БД, указывайте корректные координаты,
    потому что обновление данных о погоде происходят по координатам,
    а не по названию города"""
    data = CityDB(session=session)
    result = await data.add_city(body)
    return GetAllInfo.model_validate(result)


@app.get("/{city_id}")
@LOGER.catch
async def get_city_by_id(city_id: int,
                         session: AsyncSession = Depends(get_db)):
    """Эндпоинт возвращает конкретную запись из БД"""
    connect = CityDB(session=session)
    data = await connect.get_current_city(city_id)
    if not data:
        return HTTPException(status_code=404, detail="Empty result")
    return GetAllInfo.model_validate(data)


@app.delete("/{city_id}")
@LOGER.catch
async def delete_city(city_id: int, session: AsyncSession = Depends(get_db)):
    """Эндпоинт удаляет запись из БД"""
    con = CityDB(session=session)
    data = await con.get_current_city(city_id=city_id)
    if data:
        await con.delete_city(city_id=city_id)
        return JSONResponse(content="City has been deleted")
    return HTTPException(status_code=404, detail="Empty result")
