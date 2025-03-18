from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base
from src.config import load_config_from_redis


async def get_database_url() -> str:
    config = load_config_from_redis()
    if not config or not config.DATABASE_URL:
        raise ValueError("Database URL is not set. Ensure config is loaded.")
    return config.DATABASE_URL


async def get_db_url() -> str:
    return await get_database_url()


async def create_engine(DATABASE_URL: str):
    return create_async_engine(DATABASE_URL, echo=True)


async def get_db() -> AsyncSession:
    DATABASE_URL = await get_database_url()

    engine = await create_engine(DATABASE_URL)

    SessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)

    async with SessionLocal() as session:
        yield session


Base = declarative_base()