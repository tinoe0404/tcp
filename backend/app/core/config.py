from functools import lru_cache
from pydantic import BaseModel


class Settings(BaseModel):
    app_name: str = "TCP POS Backend"
    debug: bool = True
    env: str = "development"

    # ✅ DATABASE
    db_name: str = "tcp.db"


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
