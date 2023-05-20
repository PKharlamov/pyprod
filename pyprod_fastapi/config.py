from zoneinfo import ZoneInfo

from pydantic import BaseSettings


class Settings(BaseSettings):
    SERVER_TZ: ZoneInfo = ZoneInfo("Europe/Moscow")
    REDIS_URL: str = None


settings = Settings()
