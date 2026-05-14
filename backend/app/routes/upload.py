from fastapi import APIRouter, UploadFile, File, HTTPException
import uuid
from pathlib import Path

router = APIRouter()
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@router.post("/upload")
async def upload_svg(file: UploadFile = File(...)):
    if not file.filename.endswith('.svg'):
        raise HTTPException(status_code=400, detail="Only SVG files supported")
    contents = await file.read()
    if len(contents) > 5 * 1024 * 1024:
        raise HTTPException(status_code=400, detail="File too large")
    file_id = str(uuid.uuid4())
    path = UPLOAD_DIR / f"{file_id}.svg"
    with open(path, "wb") as f:
        f.write(contents)
    return {"fileId": file_id, "filename": file.filename, "size": len(contents)}
