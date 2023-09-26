from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Database:
    def __init__(self, db_url: str) -> None:
        self.engine = create_async_engine(db_url)
        self._session_factory = async_sessionmaker(self.engine, expire_on_commit=False)

    @property
    def session_factory(self):
        return self._session_factory
