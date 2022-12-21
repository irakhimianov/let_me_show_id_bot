from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from .base import Base


async def get_session(db_uri: str) -> AsyncSession:
    """
    Setup postgres database, creates tables if not exists. Connect to database.
    :param db_uri: postgres DSN (data source name)
    :return sessionmaker: provides to bot instance to manage sessions.
    """
    # db_uri = f'postgresql+asyncpg://{config.PG_USER}:{config.PG_PASSWORD}@{config.PG_HOST}:{config.PG_PORT}/{config.PG_DB}'
    engine = create_async_engine(url=db_uri)
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)

    sessionmaker_ = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
    async with sessionmaker_() as session:
        return session