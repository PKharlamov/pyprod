from typing import Callable
from contextlib import AbstractContextManager

from sqlalchemy.ext.asyncio import AsyncSession

from models.article import Article

from .base import PostgreSQLBaseDAL


class PostgreSQLArticleDAL(PostgreSQLBaseDAL):
    def __init__(self, session_factory: Callable[..., AbstractContextManager[AsyncSession]]):
        self.session_factory = session_factory
        super().__init__(session_factory, Article)
