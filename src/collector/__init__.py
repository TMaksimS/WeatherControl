import httpx

from settings import TOKEN, URL
from src.database.schemas import AddWeather


class Collector:
    def __init__(self):
        self.url = URL
        self.token = TOKEN

    async def get_weather_by_city(self, city: str):
        session = httpx.Client(timeout=10)
        try:
            data = session.get(
                url=f"{self.url}"
                    f"?q={city}&"
                    f"appid={self.token}"
                    f"&units=metric"
            )
        except httpx.ReadTimeout:
            data = session.get(
                url=f"{self.url}"
                    f"?q={city}"
                    f"&appid={self.token}"
                    f"&units=metric"
            )
        return data.json()

    async def get_weather_by_coord(self, lon: float, lat: float):
        session = httpx.Client(timeout=10)
        try:
            data = session.get(
                url=f"{self.url}"
                    f"?lat={lat}&lon={lon}&"
                    f"appid={self.token}"
                    f"&units=metric"
            )
        except httpx.ReadTimeout:
            data = session.get(
                url=f"{self.url}"
                    f"?lat={lat}&lon={lon}&"
                    f"appid={self.token}"
                    f"&units=metric"
            )
        return data.json()

    @staticmethod
    def parser(data: dict, city_id: int):
        result = AddWeather(
            type=data["weather"][0]["main"],
            temp=data["main"]["temp"],
            feels_like=data["main"]["feels_like"],
            wind_speed=data["wind"]["speed"],
            description=data["weather"][0]["description"],
            city_id=city_id
        )
        return result
