from fastapi import APIRouter

from .endpoints import article, user

api_router = APIRouter()
api_router.include_router(article.router)
api_router.include_router(user.router)
