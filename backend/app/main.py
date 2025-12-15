from fastapi import FastAPI  # type: ignore

from app.core.config import get_settings
from app.core.database import engine, Base
from app.api.routes.auth import router as auth_router
from app.api.routes.protected import router as protected_router



def create_app() -> FastAPI:
    settings = get_settings()

    app = FastAPI(
        title=settings.app_name,
        debug=settings.debug,
        version="0.1.0",
    )

    # ✅ Create tables on application startup
    @app.on_event("startup")
    async def on_startup():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    # ✅ Include routers
    app.include_router(
        auth_router,
        prefix="/auth",
        tags=["auth"],
    )

    app.include_router(
    protected_router,
    prefix="",
    tags=["protected"],
)


    @app.get("/health", tags=["health"])
    def health_check():
        return {
            "status": "ok",
            "env": settings.env,
        }

    return app


app = create_app()
