import asyncio

import httpx

from src.database import local_session
from src.database.schemas import AddWeather
from src.database.crud import CityDB
from src.collector import Collector
from settings import LOGER, TIME_REFRESH


async def watcher():
    """Корутина находит новые значения в БД"""
    async with local_session as session:
        connect = CityDB(session=session)
        result = await connect.get_all_id()
        await session.close()
        return [_ for _ in result]


async def get_weather(city_id: int):
    """Корутина обрашается к openweathermap.org и возвращает ответ"""
    async with local_session as session:
        connect = CityDB(session=session)
        data = await connect.get_current_city(city_id=city_id)
        await session.close()
    request = Collector()
    return await request.get_weather_by_coord(lon=data.lon, lat=data.lat)


async def update(city_id: int, data: AddWeather):
    """Корутина обновляет данные о погоде в БД"""

    async with local_session as session:
        connect = CityDB(session=session)
        result = await connect.update_weather(city_id=city_id, data=data)
        await session.close()
        return result


@LOGER.catch
async def main(time: int):
    """Мэйн корутина для запуска пстоянных обновлений городов из БД"""
    collector = Collector()
    while True:
        LOGER.info("START UPDATING CITIES")
        await asyncio.sleep(delay=5)
        cities = await watcher()
        for city in cities:
            LOGER.info(f"{city}")
            data = await get_weather(city_id=city)
            await update(city_id=city, data=collector.parser(data=data, city_id=city))
            await asyncio.sleep(delay=1.5)


if __name__ == "__main__":
    asyncio.run(main=main(TIME_REFRESH))
