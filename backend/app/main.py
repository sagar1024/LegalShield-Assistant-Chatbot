from fastapi import FastAPI
from routes import chatbot, drafting
import uvicorn

app = FastAPI(title="LegalShield Backend", description="AI-Driven Legal Chatbot API")

# Include Routes
app.include_router(chatbot.router, prefix="/chatbot", tags=["Chatbot"])
app.include_router(drafting.router, prefix="/drafting", tags=["Legal Drafting"])

@app.get("/")
def home():
    return {"message": "Welcome to the LegalShield Backend"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
