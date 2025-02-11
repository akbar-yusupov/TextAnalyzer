from os import PathLike

from pydantic import BaseModel


class AppConfig(BaseModel):
    templates: PathLike = "src/presentation/http/templates"
