from .base import BaseService
from dal import DALInterface


class UserService(BaseService):
    def __init__(self, user_dal: DALInterface):
        super().__init__(user_dal)

    async def deactivate(self, user_id: int):
        await self._dal.delete(user_id)
