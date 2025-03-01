import streamlit as st

def navbar():
    st.markdown(
        """
        <style>
            .navbar {
                background-color: #1e1e1e;  /* Dark background */
                padding: 10px;
                text-align: center;
                font-size: 20px;
                color: white;
                font-weight: bold;
                border-bottom: 2px solid #c0392b;  /* Red accent border */
            }
        </style>
        <div class="navbar">
            LegalShield — Legal Assistance Chatbot
        </div>
        """,
        unsafe_allow_html=True
    )
