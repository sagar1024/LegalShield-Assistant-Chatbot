import requests
import streamlit as st

BASE_URL = "http://127.0.0.1:8000"  # Backend's URL (hosted remotely)

def get_ai_response(query):
    """Sends query to FastAPI backend and returns AI response."""
    try:
        response = requests.post(
            f"{BASE_URL}/chatbot", 
            json={"query": query}
        )
        if response.status_code == 200:
            return response.json().get("response", "No response received.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Chatbot API Error: {e}")
        return None
        