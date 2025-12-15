from fastapi import FastAPI # type: ignore
from app.core.config import get_settings


def create_app() -> FastAPI:
    settings = get_settings()

    app = FastAPI(
        title=settings.app_name,
        debug=settings.debug,
        version="0.1.0",
    )

    @app.get("/health", tags=["health"])
    def health_check():
        return {"status": "ok", "env": settings.environment}

    return app


app = create_app()
