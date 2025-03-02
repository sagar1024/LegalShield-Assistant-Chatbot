import streamlit as st
from components.navbar import navbar
from components.footer import footer
from modules import about, faq, chatbot, legal_draft, legal_resources, summarization

# Set page config
st.set_page_config(page_title="LegalShield — AI Legal Chatbot", page_icon="⚖️", layout="wide")

# Apply custom red and dark theme CSS
st.markdown(
    """
    <style>
        /* Background color for the app */
        body {
            background-color: #1e1e1e; /* Dark background */
            color: white; /* White text */
        }

        /* Sidebar customization */
        .css-1d391kg {
            background-color: #2c3e50; /* Dark sidebar */
            color: white;
        }

        .css-1d391kg .stSidebar h1 {
            color: white;
        }

        .css-1d391kg .stSidebar .st-radio, 
        .css-1d391kg .stSidebar .stSlider, 
        .css-1d391kg .stSidebar .stButton {
            background-color: #c0392b; /* Red background for sidebar controls */
            color: white;
        }

        /* Footer color and red styling for "Hackathon" */
        .footer {
            background-color: #2c3e50; /* Dark footer */
            color: white;
            text-align: center;
            padding: 10px;
            font-size: 14px;
        }

        .footer .hackathon {
            color: #e74c3c;  /* Red color */
        }

        /* Navbar adjustments */
        .css-1d391kg .stHeader {
            background-color: #2c3e50; /* Dark navbar */
            color: white;
        }

    </style>
    """,
    unsafe_allow_html=True
)

# Navbar
navbar()

# Sidebar Navigation
st.sidebar.title("LegalShield")
page = st.sidebar.radio("Navigate to", ["About page", "Chat with LegalShield", "Legal Drafting", "Document Review" ,"FAQs", "Legal Resources"])

#Add Contact Info & Feedback in Sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("### Contact Us")
st.sidebar.markdown("""
    **Email:** support@legalshield.com
    """)

#Feedback Section
st.sidebar.markdown("### Share Your Feedback")
if st.sidebar.button("Provide Feedback"):
    st.sidebar.write("Thank you for your feedback! You can email us at feedback@legalshield.com.")

# Load the selected page
if page == "About page":
    about.show()
elif page == "Chat with LegalShield":
    chatbot.show()
elif page == "Legal Drafting":
    legal_draft.show()
elif page == "Document Review":
    summarization.render()
elif page == "FAQs":
    faq.show()
elif page == "Legal Resources":
    legal_resources.show()

# Footer
footer()
