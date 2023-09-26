import datetime
from typing import Optional
from sqlalchemy import func, String, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from db.base import Base


class Article(Base):
    __tablename__ = "article"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50), unique=True)
    content: Mapped[Optional[str]]
    is_published: Mapped[bool] = mapped_column(default=False)
    author_id: Mapped[Optional[int]] = mapped_column(ForeignKey("user.id"))
    author: Mapped["User"] = relationship(back_populates="articles")
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.CURRENT_TIMESTAMP())
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(server_default=func.CURRENT_TIMESTAMP())

    def __repr__(self) -> str:
        return f"Article(id={self.id!r}, title={self.title!r})"
