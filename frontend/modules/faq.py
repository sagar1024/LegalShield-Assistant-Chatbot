# import streamlit as st

# def show():
#     st.title("Frequently Asked Questions (FAQs)")

#     faq_list = {
#         "What kind of legal questions can I ask?": "You can ask about contracts, tenancy agreements, and basic legal rights.",
#         "Is this chatbot a replacement for a lawyer?": "No, this chatbot provides general legal guidance but is not a substitute for professional legal advice.",
#         "Can I generate legal documents?": "Yes, the chatbot can assist with basic legal document templates.",
#     }

#     for question, answer in faq_list.items():
#         with st.expander(question):
#             st.write(answer)

import streamlit as st

def show():
    st.title("Frequently Asked Questions (FAQs)")

    # Search bar for FAQ
    search_term = st.text_input("Search FAQs", "")

    # List of FAQs with answers
    faq_list = {
        "What kind of legal questions can I ask?": "You can ask about contracts, tenancy agreements, and basic legal rights.",
        "Is this chatbot a replacement for a lawyer?": "No, this chatbot provides general legal guidance but is not a substitute for professional legal advice.",
        "Can I generate legal documents?": "Yes, the chatbot can assist with basic legal document templates.",
        "How can I contact a lawyer for personalized advice?": "You can find a lawyer through local bar associations or legal service websites.",
        "Is the information provided confidential?": "While the chatbot provides information, please avoid sharing sensitive personal details for your safety.",
        "How accurate is the legal information provided?": "The information provided by the chatbot is general and should be verified with a licensed attorney for accuracy.",
        "Can the chatbot help me with international legal issues?": "The chatbot provides general guidance, but for international legal matters, it’s best to consult a lawyer with expertise in international law.",
        "Is there any cost associated with using this chatbot?": "No, using this chatbot is free. However, any legal services provided by a lawyer might incur a cost."
    }

    # Filtering FAQs based on search term
    filtered_faqs = {question: answer for question, answer in faq_list.items() if search_term.lower() in question.lower()}

    if not filtered_faqs:
        st.write("No FAQs match your search term.")
    else:
        for question, answer in filtered_faqs.items():
            with st.expander(question):
                st.write(answer)
