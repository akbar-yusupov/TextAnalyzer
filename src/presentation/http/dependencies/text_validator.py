from fastapi import UploadFile, File


async def read_text_from_upload(file: UploadFile = File(...)) -> str:
    content = await file.read()
    return content.decode("utf-8")
