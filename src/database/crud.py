from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete, insert

from src.database.models import City, Weather


class CityDB:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_city(self, city_data: dict):
        data = City(**city_data)
        self.session.add(data)
        await self.session.flush()
        stmt_weather = insert(Weather).values({"temp": 15.045, "description": "Kaif", "city_id": data.id})
        await self.session.execute(stmt_weather)
        await self.session.commit()
        return data

    async def get_all_cities(self):
        pass

    async def get_all_cities_with_weather(self):
        stmt = select(City)
        result = await self.session.scalars(stmt)
        return result.all()

    async def delete_city(self):
        pass

    async def add_weather(self, data: dict):
        stmt = insert(City.city_weather).values(**data)
        await self.session.execute(stmt)
        return stmt


class WeatherDB:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_weather(self, data: dict):
        stmt = insert(City.city_weather).values(**data)
        await self.session.execute(stmt)
        return stmt

    async def get_weather_by_id(self):
        pass

    async def delete_weather(self):
        pass
