import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from src.config import get_settings

settings = get_settings()
DATABASE_URL = settings.database_url
engine = create_async_engine(DATABASE_URL)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False)


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()




