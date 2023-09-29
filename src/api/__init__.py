from fastapi import APIRouter

from src.api.cities_handler import app as city_handler

app = APIRouter(prefix="/api")
app.include_router(city_handler)
