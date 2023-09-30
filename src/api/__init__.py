from fastapi import APIRouter

from src.api.cities_handler import app as city_handler
from src.api.weather_handler import app as weather_handler

app = APIRouter(prefix="/api")
app.include_router(city_handler)
app.include_router(weather_handler)
