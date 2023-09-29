from envparse import Env
from loguru import logger

env = Env()
env.read_envfile(".env-no-dev")
LOGER = logger
LOGER.add(
    "logs/logs.log",
    rotation="10 KB",
    format="{time} {level} {message}",
    level="ERROR"
)

DB_USER = env.str("DB_USER", default="postgres_test")
DB_PASS = env.str("DB_PASS", default="postgres_test")
DB_NAME = env.str("DB_NAME", default="postgres_test")
DB_HOST = env.str("DB_HOST", default="0.0.0.0")

REAL_DATABASE_URL = f"postgresql+asyncpg://{DB_PASS}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"
TOKEN = env.str("TOKEN", default=None)
URL = env.str("URL", default="https://api.openweathermap.org/data/2.5/weather")
APP_PORT = env.int("APP_PORT", default=8000)
APP_HOST = env.str("APP_HOST", default="0.0.0.0")
APP_RELOAD = env.bool("APP_RELOAD", default=True)
TIME_REFRESH = env.int("TIME_REFRESH", default=10)
COUNT_CITIES = env.int("COUNT_CITIES", default=50)


