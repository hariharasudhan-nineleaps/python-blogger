from fastapi import FastAPI

from src.api.blog import router as blog_router
from src.api.blog_category import router as blog_category_router
from src.db import engine

from src.models import BlogCategory, Blog

app = FastAPI(docs_url="/blogs/docs", openapi_url="/blogs/openapi.json")
app.include_router(blog_router)
app.include_router(blog_category_router)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(BlogCategory.metadata.create_all)
        await conn.run_sync(Blog.metadata.create_all)
