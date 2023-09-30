from fastapi import APIRouter

from settings import LOGER
from src.collector import Collector

app = APIRouter(prefix="/weather", tags=["weather"])


@app.get("/{city}")
@LOGER.catch
async def get_weather_by_city(city: str):
    """Эндпоинт напрямую обращается к openweathermap.org и
    возвращает ответ от сервера, Стоит учитывать что неккоректные запросы
     могут привести к зависанию приложения."""
    req = Collector()
    data = await req.get_weather_by_city(city=city)
    return data
