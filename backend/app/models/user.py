from typing import List, Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from db.base import Base


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(128), index=True, unique=True)
    password: Mapped[str] = mapped_column(String(128))
    first_name: Mapped[Optional[str]] = mapped_column(String(255), default=None)
    last_name: Mapped[Optional[str]] = mapped_column(String(255), default=None)
    is_active: Mapped[bool] = mapped_column(default=True)
    is_staff: Mapped[bool] = mapped_column(default=False)
    is_superuser: Mapped[bool] = mapped_column(default=False)

    articles: Mapped[List["Article"]] = relationship(back_populates="author")

    def __repr__(self):
        return f"User: {self.id} ({self.email})"
