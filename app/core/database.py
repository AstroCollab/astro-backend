# database.py
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

# Асинхронный URL подключения к базе данных
engine = create_async_engine("postgresql+asyncpg://cosmic_user:cosmic_password@db/cosmic_db")

async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)


@asynccontextmanager
async def get_async_session() -> AsyncSession:
    async with async_session() as session:
        yield session
