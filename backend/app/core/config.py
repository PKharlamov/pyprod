from zoneinfo import ZoneInfo
from typing import Optional
from pathlib import Path

from pydantic import PostgresDsn

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "PyProd"
    SERVER_TZ: ZoneInfo = ZoneInfo("Europe/Moscow")

    POSTGRESQL_USER: str
    POSTGRESQL_PASSWORD: str
    POSTGRESQL_HOST: str
    POSTGRESQL_PORT: int
    POSTGRESQL_DB: str

    @property
    def POSTGRES_DSN(self) -> str:
        dsn = "postgresql+asyncpg://{}:{}@{}:{}/{}".format(
            self.POSTGRESQL_USER,
            self.POSTGRESQL_PASSWORD,
            self.POSTGRESQL_HOST,
            self.POSTGRESQL_PORT,
            self.POSTGRESQL_DB
        )
        return str(PostgresDsn(dsn))

    class Config:
        env_file = Path(__file__).resolve().parents[3] / ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True
        extra = "ignore"


settings = Settings()
