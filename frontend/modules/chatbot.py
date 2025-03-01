import streamlit as st
from utils.api import get_ai_response

def show():
    st.title("LegalShield — Your favourite Legal Assistant")

    st.header("Ask Your Question")

    user_query = st.text_area("Your Question:", "")

    if st.button("Ask AI"):
        if user_query.strip():
            response = get_ai_response(user_query)
            st.subheader("AI Response:")
            st.write(response)
        else:
            st.warning("Please enter a question.")
