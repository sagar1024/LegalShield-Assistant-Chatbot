import requests
from config import GEMINI_API_KEY

def get_ai_response(query: str) -> str:
    url = "https://api.gemini.com/generate"
    headers = {"Authorization": f"Bearer {GEMINI_API_KEY}"}
    data = {"query": query}
    
    response = requests.post(url, json=data, headers=headers)
    return response.json().get("generated_response", "Sorry, I couldn't process that request.")
