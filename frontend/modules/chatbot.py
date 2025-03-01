import streamlit as st
from utils.api import get_ai_response

def show():
    st.title("LegalShield — Your Favourite Legal Assistant")

    st.subheader("Chat Interface")

    # Initialize session state for chat history
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []

    # User input field
    user_query = st.text_input("Your Question", placeholder="Type your question here...")

    if st.button("Ask AI"):
        if user_query.strip():
            # Call AI API to get response
            response = get_ai_response(user_query)

            if response:
                # Append user query and bot response to chat history
                st.session_state["chat_history"].append({"user": user_query, "bot": response})
            else:
                st.error("Failed to get a response from the chatbot. Please try again.")
        else:
            st.warning("Please enter a question.")

    # Display chat history
    if st.session_state["chat_history"]:
        for chat in st.session_state["chat_history"]:
            st.write(f"**You**: {chat['user']}")
            st.write(f"**Bot**: {chat['bot']}")
            st.markdown("---")

    # Clear chat history
    if st.button("Clear Chat"):
        st.session_state["chat_history"] = []
        st.success("Chat history cleared.")
