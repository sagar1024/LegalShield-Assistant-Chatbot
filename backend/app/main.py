from fastapi import FastAPI
from app.routes import chatbot, drafting

app = FastAPI(title="LegalShield Backend", description="AI-Driven Legal Chatbot API")

# Include Routes
app.include_router(chatbot.router)
app.include_router(drafting.router)

@app.get("/")
def home():
    return {"message": "Welcome to the LegalShield Backend"}
