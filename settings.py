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

DB_USER = env.str("DB_USER", default="postgres_test")
DB_PASS = env.str("DB_PASS", default="postgres_test")
DB_NAME = env.str("DB_NAME", default="postgres_test")
DB_HOST = env.str("DB_HOST", default="localhost")
TOKEN = env.str("TOKEN", default=None)
URL = env.str("URL", default="http://api.openweathermap.org/data/2.5/weather")
APP_PORT = env.int("APP_PORT", default=8000)
APP_HOST = env.str("APP_HOST", default="0.0.0.0")
APP_RELOAD = env.bool("APP_RELOAD", default=True)
COUNT_CITIES = env.int("COUNT_CITIES", default=50)
TIME_REFRESH = env.int("TIME_REFRESH", default=60)
REAL_DATABASE_URL = env.str(
    "REAL_DATABASE_URL",
    default=f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"
)
