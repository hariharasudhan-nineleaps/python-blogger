from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from src.config import get_settings

settings = get_settings()
engine = create_async_engine(settings.database_url)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False)

async def get_db():
    try:
        conn = SessionLocal()
        yield conn
    finally:
        await conn.close()