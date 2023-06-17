import uuid
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi.routing import APIRouter
from fastapi import Depends

from src.db import get_db
from src.api.types.blog_category import CreateBlogCategoryRequest
from src.models.blog_category import BlogCategory

router = APIRouter(prefix="/blog-categories")


@router.post("/")
async def create_blog_category(request_body :CreateBlogCategoryRequest,session: Annotated[AsyncSession, Depends(get_db)]):
    db_data = {"id": uuid.uuid4().hex, **request_body.dict()}
    blog_category = BlogCategory(**db_data)
    
    async with session.begin():
        session.add(blog_category)
        await session.commit()

    return {"id": blog_category.id}