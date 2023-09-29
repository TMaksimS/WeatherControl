from pydantic import BaseModel, ConfigDict


class MyModel(BaseModel):
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)


class GetWeather(MyModel):
    type: str
    temp: float
    feels_like: float
    wind_speed: float
    description: str


class AddWeather(GetWeather):
    city_id: int


class CreateData(BaseModel):
    name: str | None
    country: str | None
    lon: float
    lat: float


class GetCity(MyModel):
    id: int
    name: str
    country: str
    lon: float
    lat: float


class GetAllInfo(GetCity):
    city_weather: GetWeather | None


class GetAllData(BaseModel):
    data: list
