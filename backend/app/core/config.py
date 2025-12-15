from functools import lru_cache
from pydantic import BaseModel


class Settings(BaseModel):
    app_name: str = "TCP POS Backend"
    debug: bool = True
    env: str = "development"

    # ✅ DATABASE
    db_name: str = "tcp.db"

# Security / JWT
    JWT_SECRET_KEY: str = "CHANGE_ME_IN_PRODUCTION"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
