from fastapi import APIRouter
from schemas import ChatbotRequest, ChatbotResponse
from services.chatbot import get_ai_response

router = APIRouter()

@router.post("/", response_model=ChatbotResponse)
def chatbot(request: ChatbotRequest):
    response = get_ai_response(request.query)
    return {"response": response}
