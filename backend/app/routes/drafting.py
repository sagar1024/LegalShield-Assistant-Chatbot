from fastapi import APIRouter
from app.schemas import DraftingRequest
from app.services.drafting import generate_legal_document

router = APIRouter()

@router.post("/")
def draft_document(request: DraftingRequest):
    document_text = generate_legal_document(request.document_type, request.details)
    return {"document": document_text}
