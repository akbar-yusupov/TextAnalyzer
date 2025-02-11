from fastapi import FastAPI

from src.presentation.http.routers.text_analyzer import text_analyzer_router


def include_routers(app: FastAPI) -> None:
    app.include_router(
        text_analyzer_router,
        tags=[
            "text_analyzer",
        ],
    )
