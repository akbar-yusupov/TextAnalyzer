from fastapi import APIRouter, Depends
from fastapi.requests import Request
from fastapi.responses import HTMLResponse

from src.application.text_service import analyze_text
from src.presentation.http.dependencies.text_validator import \
    read_text_from_upload

text_analyzer_router = APIRouter()


@text_analyzer_router.get("/health", tags=["health"])
async def health():
    return {"status": "OK"}


@text_analyzer_router.get("/", response_class=HTMLResponse)
async def upload_form(request: Request):
    return request.app.state.templates.TemplateResponse(
        "upload.html", {"request": request}
    )


@text_analyzer_router.post("/upload", response_class=HTMLResponse)
async def handle_upload(request: Request, file_text: str = Depends(read_text_from_upload)):
    results = analyze_text(file_text)
    return request.app.state.templates.TemplateResponse(
        "results.html", {"request": request, "results": results}
    )
