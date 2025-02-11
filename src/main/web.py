from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

from src import presentation # noqa
from src.main.config import AppConfig


def create_app() -> FastAPI:
    _app = FastAPI()
    presentation.include_routers(_app)
    _app.state.config = AppConfig()
    _app.state.templates = Jinja2Templates(
        directory=_app.state.config.templates
    )
    return _app


app = create_app()
