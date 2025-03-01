import requests

BACKEND_URL = "http://127.0.0.1:8000"

def get_ai_response(query):
    """Sends query to FastAPI backend and returns AI response."""
    try:
        response = requests.post(f"{BACKEND_URL}/chat", json={"query": query})
        return response.json().get("response", "No response received.")
    except requests.exceptions.RequestException:
        return "Error connecting to AI service."
