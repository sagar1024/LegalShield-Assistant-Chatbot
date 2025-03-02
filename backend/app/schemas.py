from pydantic import BaseModel

# Schema for chatbot request
class ChatbotRequest(BaseModel):
    query: str

# Schema for chatbot response
class ChatbotResponse(BaseModel):
    response: str

# Schema for legal document drafting
class DraftingRequest(BaseModel):
    document_type: str
    details: dict
