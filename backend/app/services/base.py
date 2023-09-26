from typing import Any

from pydantic import BaseModel

from dal import DALInterface


class BaseService:
    def __init__(self, dal: DALInterface):
        self._dal = dal

    async def get_all(self) -> list[BaseModel]:
        return await self._dal.select_all()

    async def get_by_id(self, model_id: Any) -> BaseModel | None:
        return await self._dal.select_by_id(model_id=model_id)

    async def create(self, dto: BaseModel) -> BaseModel:
        return await self._dal.insert(dto=dto)

    async def update(self, model_id: Any, dto: BaseModel) -> BaseModel:
        if not self.get_by_id(model_id):
            raise ValueError(f"Entity with ID {model_id} not found.")
        return await self._dal.update(model_id=model_id, dto=dto)

    async def delete(self, model_id: Any) -> bool:
        return await self._dal.delete(model_id=model_id)
