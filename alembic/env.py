from logging.config import fileConfig
import logging

from alembic import context

from sqlalchemy import engine_from_config, pool
from sqlalchemy.orm import sessionmaker

from src import Base
from src.user import User
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


def run_migrations_online():
    engine = engine_from_config(
        config.get_section("alembic"),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool
    )

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    with engine.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()


run_migrations_online()
