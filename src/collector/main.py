import typing

import requests

from settings import TOKEN, URL


def get_weather_by_city(city: str) -> typing.Any:
    data = requests.get(url=f"{URL}?q={city}&appid={TOKEN}&units=metric")
    return data.json()


def get_weather_by_coord(lon: float, lat: float) -> typing.Any:
    data = requests.get(url=f"{URL}?lat={lat}&lon={lon}&appid={TOKEN}&units=metric")
    return data.json()


if __name__ == "__main__":
    # print(get_weather_by_city(str(input())))
    print(get_weather_by_city(city="Saratov"))