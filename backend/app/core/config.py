from pydantic import BaseModel
from functools import lru_cache


class Settings(BaseModel):
    app_name: str = "TCP POS Backend"
    debug: bool = True
    env: str = "development"

    # Database
    db_name: str = "tcp.db"


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
