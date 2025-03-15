import asyncio
from logging.config import fileConfig
import logging

from sqlalchemy import pool
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import async_engine_from_config

from alembic import context

from src import Base
from src.user import User
from src.metro import Station, Line, metro_match
from src.subscription import Subscription, SubscriptionType
from src.trade import Item, Service, Trade

from src.config import load_config_from_redis

target_metadata = Base.metadata
config = context.config

def get_database_url():
    config_redis = load_config_from_redis()
    if not config_redis or not config_redis.DATABASE_URL:
        raise ValueError("Database URL is not set. Ensure config is loaded.")
    logging.info(f"Using database URL: {config_redis.DATABASE_URL}")
    return config_redis.DATABASE_URL

config.set_main_option('sqlalchemy.url', get_database_url())
fileConfig(config.config_file_name)


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection: Connection) -> None:
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()


async def run_async_migrations() -> None:
    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


def run_migrations_online() -> None:
    asyncio.run(run_async_migrations())


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
