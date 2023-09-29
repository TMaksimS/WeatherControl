from envparse import Env
from loguru import logger

env = Env()
env.read_envfile(".env")
LOGER = logger
LOGER.add(
    "logs/logs.log",
    rotation="10 KB",
    format="{time} {level} {message}",
    level="ERROR"
)

REAL_DATABASE_URL = env.str(
    "REAL_DATABASE_URL",
    default="postgresql+asyncpg://postgres_test:postgres_test@0.0.0.0:5432/postgres_test"
)
TOKEN = env.str("TOKEN", default=None)
URL = env.str("URL", default="https://api.openweathermap.org/data/2.5/weather")
APP_PORT = env.int("APP_PORT", default=8000)
APP_HOST = env.str("APP_HOST", default="0.0.0.0")
APP_RELOAD = env.bool("APP_RELOAD", default=True)
TIME_REFRESH = env.int("TIME_REFRESH", default=60)
COUNT_CITIES = env.int("COUNT_CITIES", default=50)


