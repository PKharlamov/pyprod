from dependency_injector import containers, providers

from core.config import settings
from db.base import Database
from dal import (
    PostgreSQLArticleDAL,
    PostgreSQLUserDAL,
)
from services import (
    ArticleService,
    UserService
)


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "api.v1.endpoints.article",
            "api.v1.endpoints.user",
            # "core.security",
            # "core.dependency",
        ]
    )

    db = providers.Singleton(Database, db_url=str(settings.POSTGRES_DSN))

    # DALs
    article_dal = providers.Factory(PostgreSQLArticleDAL, session_factory=db.provided.session_factory)
    user_dal = providers.Factory(PostgreSQLUserDAL, session_factory=db.provided.session_factory)

    # Services
    article_service = providers.Factory(ArticleService, article_dal=article_dal)
    user_service = providers.Factory(UserService, user_dal=user_dal)
