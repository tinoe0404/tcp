from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.engine import URL
from sqlalchemy.orm import DeclarativeBase

from app.core.config import settings


# ✅ Base declaration (from the screenshot)
class Base(DeclarativeBase):
    pass


DATABASE_URL = URL.create(
    drivername="sqlite+aiosqlite",
    database=settings.db_name,
)

engine = create_async_engine(
    DATABASE_URL,
    echo=settings.debug,
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session
