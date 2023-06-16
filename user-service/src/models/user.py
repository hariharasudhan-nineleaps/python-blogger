from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional
from sqlalchemy import String
from sqlalchemy import func
import datetime

from .base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String(100), primary_key=True, autoincrement=False)
    name: Mapped[Optional[str]] = mapped_column(String(200))
    email: Mapped[str] = mapped_column(String(200), unique=True)
    username: Mapped[str] = mapped_column(String(100), unique=True)
    password_hash: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())

    def __str__(self) -> str:
        return f'${self.id} - ${self.name} - ${self.email}'