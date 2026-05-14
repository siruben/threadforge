from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from pathlib import Path
from ..services.svg_parser import parse_svg
from ..services.stitch_generator import generate_stitches
from ..services.pes_exporter import export_pes

router = APIRouter()
UPLOAD_DIR = Path("uploads")
EXPORT_DIR = Path("exports")
EXPORT_DIR.mkdir(exist_ok=True)

class ConversionRequest(BaseModel):
    fileId: str
    density: float = 1.0
    minStitchLength: int = 2
    maxStitchLength: int = 20
    stitchType: str = "satin"
    fabric: str = "cotton"
    threadColor: str = "#c39b69"

@router.post("/convert")
async def convert(request: ConversionRequest):
    file_path = UPLOAD_DIR / f"{request.fileId}.svg"
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="SVG not found")
    svg_paths = parse_svg(str(file_path))
    stitches = generate_stitches(svg_paths, density=request.density, min_stitch_length=request.minStitchLength, max_stitch_length=request.maxStitchLength, stitch_type=request.stitchType, fabric=request.fabric)
    pes_file = EXPORT_DIR / f"{request.fileId}.pes"
    export_pes(stitches, str(pes_file), request.threadColor)
    return {"status":"success", "file": str(pes_file)}
