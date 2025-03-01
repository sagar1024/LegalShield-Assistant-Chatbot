import streamlit as st

def show():
    st.title("About LegalShield Chatbot")
    st.write("""
        This AI-driven chatbot is designed to assist users in understanding legal documents and rights.
        
        **Key Features:**
        - Instant AI responses to legal queries
        - Assistance with legal document drafting
        - Simple and accessible user interface

        This project is built using:
        - **Streamlit** for the frontend
        - **FastAPI** as the backend
        - **Gemini API** for AI-powered legal assistance
    """)
