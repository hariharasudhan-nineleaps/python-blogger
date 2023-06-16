from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    jwt_secret: str

    class Config:
        extra = 'ignore'
        env_file = '.env'

@lru_cache()
def get_settings() -> Settings:
    return Settings()