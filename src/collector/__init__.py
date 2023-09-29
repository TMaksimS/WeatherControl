import typing
import requests

from settings import TOKEN, URL
from src.database.schemas import AddWeather


class Collector:
    def __init__(self):
        self.url = URL
        self.token = TOKEN

    def get_weather_by_city(self, city: str) -> typing.Any:
        data = requests.get(url=f"{self.url}?q={city}&appid={self.token}&units=metric")
        return data.json()

    def get_weather_by_coord(self, lon: float, lat: float) -> typing.Any:
        data = requests.get(url=f"{self.url}?lat={lat}&lon={lon}&appid={self.token}&units=metric")
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
