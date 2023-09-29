from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete, update

from src.database.models import City, Weather
from src.database.schemas import GetWeather, CreateData
from src.collector import Collector


class CityDB:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_city(self, city_data: CreateData):
        data = City(**city_data.model_dump())
        self.session.add(data)
        await self.session.flush()
        collector = Collector()
        weather_data = collector.get_weather_by_coord(
            lon=data.lon,
            lat=data.lat
        )
        data.city_weather = Weather(
            **collector.parser(
                data=weather_data,
                city_id=data.id
            ).dict()
        )
        await self.session.commit()
        return data

    async def get_current_city(self, city_id: int):
        stmt = select(City).where(City.id == city_id)
        data = await self.session.scalar(stmt)
        return data

    async def get_all_cities_with_weather(self):
        stmt = select(City)
        result = await self.session.scalars(stmt)
        return result.all()

    async def delete_city(self, city_id: int):
        stmt = delete(City).where(City.id == city_id)
        await self.session.execute(stmt)
        await self.session.commit()
        return True

    async def get_all_id(self):
        stmt = select(City.id)
        result = await self.session.scalars(stmt)
        return result.all()

    async def update_weather(self, city_id: int, data: GetWeather):
        stmt = update(
            Weather
        ).where(
            Weather.city_id == city_id
        ).values(
            **data.model_dump()
        )
        await self.session.execute(stmt)
        obj = await self.session.get(City, city_id)
        await self.session.close()
        return obj
