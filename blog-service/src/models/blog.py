import datetime
import enum
from typing import Optional, List


from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, func, ForeignKey
from sqlalchemy.dialects.postgresql import ARRAY, ENUM

from .base import Base
from .blog_category import BlogCategory

from src.config.table_name import BLOG_TABLE_NAME, BLOG_CATEGORY_TABLE_NAME


class Status(enum.Enum):
    ACTIVE = "active"
    DRAFT = "draft"


class Blog(Base):
    __tablename__  = BLOG_TABLE_NAME

    id: Mapped[str] = mapped_column(String(100), primary_key=True, autoincrement=False)
    title: Mapped[str] = mapped_column(String(200))
    description: Mapped[Optional[str]] = mapped_column(Text())
    status: Mapped[Status] = mapped_column(default=Status.DRAFT)
    tags: Mapped[List[str]] = mapped_column(ARRAY(String))
    user_id: Mapped[str] = mapped_column(String(100), index=True)

    category_id: Mapped[int] = mapped_column(ForeignKey(f"{BLOG_CATEGORY_TABLE_NAME}.id"))
    category: Mapped["BlogCategory"] = relationship()


    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now(), server_onupdate=func.now())