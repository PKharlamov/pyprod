from typing import Optional
from datetime import datetime

from pydantic import BaseModel


class ArticleDTO(BaseModel):
    id: int
    title: str
    content: Optional[str]
    is_published: bool
    author_id: Optional[int]
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True


class ArticleCreateDTO(BaseModel):
    title: str
    content: Optional[str]


class ArticleUpdateDTO(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
