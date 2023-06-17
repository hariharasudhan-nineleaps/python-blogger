import uuid
from fastapi.routing import APIRouter
from fastapi import Depends
from src.api.types.blog import BlogCreateRequest
from typing import Annotated, Any
from sqlalchemy.ext.asyncio import AsyncSession

from src.db import get_db
from src.api.types.token import TokenData
from src.auth import get_current_user

from src.api.types.response import APIResponse
from src.api.types.blog import BlogItem

router = APIRouter(prefix="/blogs")


@router.post("", response_model=APIResponse[Any, None])
async def create_blog(request_body: BlogCreateRequest, session: Annotated[AsyncSession, Depends(get_db)], user: Annotated[TokenData, Depends(get_current_user)]):
    db_data = {
        **request_body.dict(),
        "id": uuid.uuid4().hex,
        "user_id": user.user_id
    }
    async with session.begin():
        pass
    
    return APIResponse(data=db_data)


@router.get("/{blog_id}")
async def get_blog(blog_id: str, session: Annotated[AsyncSession, Depends(get_db)], user: Annotated[TokenData, Depends(get_current_user)]):
    return {blog_id: blog_id}


@router.patch("/{blog_id}")
async def update_status(blog_id: str, session: Annotated[AsyncSession, Depends(get_db)], user: Annotated[TokenData, Depends(get_current_user)]):
    return {blog_id: blog_id}


@router.delete("/{blog_id}")
async def delete_blog(blog_id: str, session: Annotated[AsyncSession, Depends(get_db)], user: Annotated[TokenData, Depends(get_current_user)]):
    return {blog_id: blog_id}