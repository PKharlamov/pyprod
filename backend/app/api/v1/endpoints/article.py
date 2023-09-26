from fastapi import APIRouter, Depends, status
from dependency_injector.wiring import Provide, inject

from schemas.article import ArticleDTO, ArticleCreateDTO, ArticleUpdateDTO
from services.article import ArticleService
from core.container import Container

router = APIRouter(prefix="/article", tags=["article"])


@router.get("/{article_id}", response_model=ArticleDTO)
@inject
async def get_article(article_id: int, service: ArticleService = Depends(Provide[Container.article_service])):
    return await service.get_by_id(article_id)


@router.get("", response_model=list[ArticleDTO])
@inject
async def get_articles(service: ArticleService = Depends(Provide[Container.article_service])):
    return await service.get_all()


@router.post("", response_model=ArticleDTO, status_code=status.HTTP_201_CREATED)
@inject
async def create_article(
    article: ArticleCreateDTO,
    service: ArticleService = Depends(Provide[Container.article_service])
):
    return await service.create(article)


@router.patch("/{article_id}", response_model=ArticleDTO, status_code=status.HTTP_200_OK)
@inject
async def update_article(
    article_id: int,
    article: ArticleUpdateDTO,
    service: ArticleService = Depends(Provide[Container.article_service]),
):
    return await service.update(model_id=article_id, dto=article)


@router.delete("/{article_id}", status_code=status.HTTP_204_NO_CONTENT)
@inject
async def delete_article(article_id: int, service: ArticleService = Depends(Provide[Container.article_service])):
    await service.delete(model_id=article_id)
