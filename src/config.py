from pydantic_core.core_schema import computed_field
from redis import Redis
import json
from pydantic import Field
from pydantic_settings import BaseSettings
from fastapi import APIRouter

router = APIRouter()


class Config(BaseSettings):
    POSTGRES_USER: str = Field(..., env="POSTGRES_USER")
    POSTGRES_PASSWORD: str = Field(..., env="POSTGRES_PASSWORD")
    POSTGRES_NAME: str = Field(..., env="POSTGRES_NAME")
    POSTGRES_HOST: str = Field(..., env="POSTGRES_HOST")
    POSTGRES_PORT: int = Field(..., env="POSTGRES_PORT", strict=False)
    SECRET_KEY: str = Field(..., env="SECRET_KEY")
    DEBUG: bool = Field(False, env="DEBUG")
    REDIS_URL: str = Field(..., env="REDIS_URL")
    ALGORITHM: str = Field(..., env="ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: str = Field(..., env="ACCESS_TOKEN_EXPIRE_MINUTES", strict=False)

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_NAME}"

    def to_dict(self) -> dict:
        return self.model_dump()


def load_config_from_redis():
    config = Config()
    redis = Redis.from_url(config.REDIS_URL)
    config_data = redis.get("config")

    if config_data is not None:
        return Config(**json.loads(config_data))

    redis.set("config", json.dumps(config.to_dict()), ex=3600)
    return config



