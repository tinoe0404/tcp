import pytest # type: ignore
from sqlalchemy import text # type: ignore

from app.core.database import engine


@pytest.mark.anyio
async def test_database_connection():
    async with engine.begin() as conn:
        result = await conn.execute(text("SELECT 1"))
        assert result.scalar() == 1
