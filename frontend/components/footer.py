import streamlit as st

def footer():
    st.markdown(
        """
        <style>
            .footer {
                position: fixed;
                bottom: 0;
                left: 0;
                width: 100%;
                background-color: #1e1e1e;  /* Dark background */
                color: white;
                text-align: center;
                padding: 10px;
                font-size: 14px;
                display: flex;
                justify-content: center;
                align-items: center;
                border-top: 2px solid #c0392b;  /* Red accent border */
            }
            .footer .hackathon {
                color: #e74c3c;  /* Lighter red for 'Hackathon' */
            }
        </style>
        <div class="footer">
            © 2025 LegalShield. All rights reserved. | <span class="hackathon">Hackathon 2025</span>
        </div>
        """,
        unsafe_allow_html=True
    )
