from abc import ABC, abstractmethod
from typing import Any, Callable
from contextlib import AbstractContextManager

from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from core.exceptions import DuplicatedError, NotFoundError


class DALInterface(ABC):
    @abstractmethod
    async def select_all(self) -> list[BaseModel]:
        pass

    @abstractmethod
    async def select_by_id(self, model_id: Any) -> BaseModel:
        pass

    @abstractmethod
    async def insert(self, dto: BaseModel) -> BaseModel:
        pass

    @abstractmethod
    async def update(self, model_id: Any, dto: BaseModel) -> BaseModel:
        pass

    @abstractmethod
    async def delete(self, model_id: Any) -> bool:
        pass


class PostgreSQLBaseDAL(DALInterface):
    def __init__(self, session_factory: Callable[..., AbstractContextManager[AsyncSession]], model) -> None:
        self.session_factory = session_factory
        self._model = model
        self._model_name = self._model.__name__

    async def select_all(self):
        async with self.session_factory() as session:
            query = select(self._model)
            query_result = await session.execute(query)
            found_model_list = query_result.scalars().all()
            return found_model_list

    async def select_by_id(self, model_id: int):
        async with self.session_factory() as session:
            query = select(self._model).where(self._model.id == model_id)
            query_result = await session.execute(query)
            found_model = query_result.scalar()
            if not found_model:
                raise NotFoundError(detail=f"not found model name: {self._model_name}, requested id: {model_id}")
            return found_model

    async def insert(self, dto):
        async with self.session_factory() as session:
            model = self._model(**dto.dict())
            try:
                session.add(model)
                await session.commit()
                await session.refresh(model)
            except IntegrityError as e:
                raise DuplicatedError(detail=str(e.orig)) from e
            return model

    async def update(self, model_id: int, dto: BaseModel):
        async with self.session_factory() as session:
            found_model = await self.select_by_id(model_id)
            for key, value in dto.dict().items():
                if value is None:
                    continue
                setattr(found_model, key, value)
            await session.merge(found_model)
            await session.commit()
            return await self.select_by_id(model_id)

    async def upsert(self, model_id: int, dto: BaseModel):
        try:
            await self.select_by_id(model_id)
        except NotFoundError:
            return await self.insert(dto)
        return self.update(model_id=model_id, dto=dto)

    async def delete(self, model_id: int):
        async with self.session_factory() as session:
            found_model = await self.select_by_id(model_id)
            if not found_model:
                raise NotFoundError(detail=f"not found model name: {self._model_name}, requested id: {model_id}")
            await session.delete(found_model)
            await session.commit()
