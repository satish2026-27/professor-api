from fastapi import APIRouter, UploadFile, File, Depends
from fastapi.responses import JSONResponse
from app.api.deps import auth_guard
import csv, io

router = APIRouter(prefix="/files", tags=["files"])

@router.post("/upload", dependencies=[Depends(auth_guard)])
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    info = {"filename": file.filename, "content_type": file.content_type, "size": len(content)}

    preview = None
    try:
        text = content.decode("utf-8", errors="ignore")
        reader = csv.DictReader(io.StringIO(text))
        preview = [row for _, row in zip(range(5), reader)]
    except Exception:
        pass

    return JSONResponse({"ok": True, "file": info, "csv_preview": preview})
