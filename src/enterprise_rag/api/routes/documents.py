
from fastapi import APIRouter, File, HTTPException, UploadFile

from enterprise_rag.ingestion.pdf_parser import extract_pdf


router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)

@router.post("/upload-multiple")
async def upload_multiple(files: list[UploadFile] = File(...)) -> dict :

    extracted_files = []
    for file in files:
        if file.content_type != "application/pdf":
            raise HTTPException(
                status_code=415,
                detail="hanya menerima pdf"
            )
        content = await file.read()
        if not content.startswith(b"%PDF-"):
            raise HTTPException(
                status_code=400,
                detail="file tidak valid/rusak"
            )
        
        try:
            pages = extract_pdf(content)
            extracted_files.append(pages)
        except Exception as e:
            raise HTTPException(
                status_code=422,
                detail=f"Terjadi kesalahan parsing data: {e}"
            ) from e

    return {
            "message": "berhasil",
            "data": extracted_files
        }
        
