import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, func

from .base import Base
from src.config.table_name import BLOG_CATEGORY_TABLE_NAME

class BlogCategory(Base):

    __tablename__ = BLOG_CATEGORY_TABLE_NAME

    id: Mapped[str] = mapped_column(String(100), primary_key=True, autoincrement=False)
    name: Mapped[str] = mapped_column(String(200))
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(server_onupdate=func.now())
