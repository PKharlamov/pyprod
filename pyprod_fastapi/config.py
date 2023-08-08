from zoneinfo import ZoneInfo

from pydantic import BaseSettings


class Settings(BaseSettings):
    SERVER_TZ: ZoneInfo = ZoneInfo("Europe/Moscow")
    REDIS_HOST: str = "redis"
    REDIS_PORT: str = "6379"


settings = Settings()
