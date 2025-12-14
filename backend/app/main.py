from fastapi import FastAPI # type: ignore


def create_app() -> FastAPI:
    app = FastAPI(
        title="TCP POS Backend",
        version="0.1.0",
    )

    @app.get("/health", tags=["health"])
    def health_check():
        return {"status": "ok"}

    return app


app = create_app()
