from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url: str
    auth_service_url: str

    class Config:
        extra = 'ignore'
        env_file = '.env'


@lru_cache()
def get_settings() -> Settings:
    return Settings()
