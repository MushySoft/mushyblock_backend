from redis import Redis
import json
from pydantic import Field
from pydantic_settings import BaseSettings
from fastapi import APIRouter

router = APIRouter()


class Config(BaseSettings):
    USER: str = Field(..., env="USER")
    PASSWORD: str = Field(..., env="PASSWORD")
    NAME: str = Field(..., env="NAME")
    HOST: str = Field(..., env="HOST")
    PORT: int = Field(..., env="PORT")
    SECRET_KEY: str = Field(..., env="SECRET_KEY")
    DEBUG: bool = Field(False, env="DEBUG")
    REDIS_URL: str = Field(..., env="REDIS_URL")
    ALGORITHM: str = Field(..., env="ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: str = Field(..., env="ACCESS_TOKEN_EXPIRE_MINUTES")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    @property
    def DATABASE_URL(self):
        return f"postgresql+psycopg2://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.NAME}"

    @property
    def ASYNC_DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.NAME}"

    def to_dict(self) -> dict:
        return self.dict()


def load_config_from_redis():
    config = Config()
    redis = Redis.from_url(config.REDIS_URL)
    config_data = redis.get("config")

    if config_data:
        return Config(**json.loads(config_data))

    redis.set("config", json.dumps(config.to_dict()), ex=3600)
    return config



