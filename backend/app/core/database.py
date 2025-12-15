from sqlalchemy.ext.asyncio import (  # type: ignore
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.engine import URL  # type: ignore

from app.core.config import settings


DATABASE_URL = URL.create(
    drivername="sqlite+aiosqlite",
    database=settings.db_name,   # ✅ lowercase
)

engine = create_async_engine(
    DATABASE_URL,
    echo=settings.debug,         # ✅ lowercase
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session
