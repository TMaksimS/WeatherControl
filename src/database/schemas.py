from pydantic import BaseModel, ConfigDict


class MyModel(BaseModel):
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)


class GetWeather(MyModel):

    temp: float
    description: str


class CreateData(BaseModel):
    name: str
    country: str


class GetCity(MyModel):

    id: int
    name: str
    country: str


class GetAllInfo(GetCity):
    city_weather: GetWeather | None


class GetAllData(GetAllInfo):
    data: list
