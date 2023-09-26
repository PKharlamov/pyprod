from .base import BaseService
from dal import DALInterface


class ArticleService(BaseService):
    def __init__(self, article_dal: DALInterface):
        super().__init__(article_dal)
