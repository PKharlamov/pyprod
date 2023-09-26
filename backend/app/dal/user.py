from typing import Callable
from contextlib import AbstractContextManager

from sqlalchemy.ext.asyncio import AsyncSession

from models.user import User
from core.exceptions import NotFoundError

from .base import PostgreSQLBaseDAL


class PostgreSQLUserDAL(PostgreSQLBaseDAL):
    def __init__(self, session_factory: Callable[..., AbstractContextManager[AsyncSession]]):
        self.session_factory = session_factory
        super().__init__(session_factory, User)

    async def delete(self, model_id: int):
        async with self.session_factory() as session:
            user = await self.select_by_id(model_id)
            if not user:
                raise NotFoundError(detail=f"not found model name: {self._model_name}, requested id: {model_id}")
            user.is_active = False
            await session.commit()
