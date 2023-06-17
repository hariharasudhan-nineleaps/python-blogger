from typing import List
from pydantic import BaseModel

from src.models.blog import Status
from .blog_category import BlogCategoryItem

class BlogItem(BaseModel):
    id: str
    title: str
    description: str
    tags: List[str]
    #category: BlogCategoryItem
    category_id: str
    user_id: str

    class Config:
        orm_mode = True

class BlogCreateRequest(BaseModel):
    title: str
    description: str
    tags: List[str]
    category_id: str


