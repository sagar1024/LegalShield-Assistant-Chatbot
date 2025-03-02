from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.drafting import generate_legal_document

router = APIRouter()

class DraftRequest(BaseModel):
    document_type: str
    details: dict  

@router.post("/draft")
async def draft_document(request: DraftRequest):
    try:
        pdf_path = generate_legal_document(request.document_type, request.details)
        return {"message": "Document generated successfully", "pdf_url": pdf_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating document: {str(e)}")
