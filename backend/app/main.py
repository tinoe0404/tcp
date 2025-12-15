from fastapi import FastAPI  # type: ignore
from app.core.config import get_settings
from app.api.routes.auth import router as auth_router


def create_app() -> FastAPI:
    settings = get_settings()

    app = FastAPI(
        title=settings.app_name,
        debug=settings.debug,
        version="0.1.0",
    )

    # ✅ Include routers here
    app.include_router(auth_router)

    @app.get("/health", tags=["health"])
    def health_check():
        return {"status": "ok", "env": settings.env}

    return app


app = create_app()
