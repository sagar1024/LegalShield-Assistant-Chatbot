import streamlit as st
from utils.api import get_ai_response

def show():
    st.title("LegalShield — Your Favourite Legal Assistant")

    # Initialize chat history
    chat_history = st.session_state.setdefault("chat_history", [])

    # User input
    user_query = st.text_input("Ask your question:", placeholder="Type here...")

    # Ask AI button
    if st.button("Ask AI") and user_query.strip():
        response = get_ai_response(user_query)
        #print(response) #Debugging
        
        chat_history.append({"user": user_query, "bot": response})

    # Display chat history
    for chat in chat_history:
        st.write(f"**You**: {chat['user']}")
        st.write(f"**Bot**: {chat['bot']}")
        st.markdown("---")

    # Clear chat button
    if st.button("Clear Chat"):
        chat_history.clear()
        st.success("Chat history cleared.")
