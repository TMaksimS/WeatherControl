from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from settings import REAL_DATABASE_URL

engine = create_async_engine(
    REAL_DATABASE_URL,
    echo=False
)

async_session_maker = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)

local_session = AsyncSession(engine)


class Base(DeclarativeBase):
    pass


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    try:
        async with async_session_maker() as session:
            yield session
    finally:
        await session.close()
