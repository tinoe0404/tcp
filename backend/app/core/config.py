from pydantic import BaseModel # type: ignore
from dotenv import load_dotenv # type: ignore
import os

load_dotenv()


class Settings(BaseModel):
    app_name: str = "TCP POS Backend"
    environment: str = "development"
    debug: bool = True


def get_settings() -> Settings:
    return Settings(
        app_name=os.getenv("APP_NAME", "TCP POS Backend"),
        environment=os.getenv("ENVIRONMENT", "development"),
        debug=os.getenv("DEBUG", "true").lower() == "true",
    )
