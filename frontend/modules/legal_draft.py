import streamlit as st
from utils.api import draft_legal_document

def show():
    st.title("Legal Document Drafting")

    document_type = st.selectbox("Select Document Type", ["Contract", "Will", "Non-Disclosure Agreement (NDA)", "Other"])
    
    details = {}

    if document_type == "Contract":
        details["party_one"] = st.text_input("Party 1")
        details["party_two"] = st.text_input("Party 2")
        details["contract_terms"] = st.text_area("Contract Terms")
    elif document_type == "Will":
        details["testator_name"] = st.text_input("Testator's Name")
        details["beneficiaries"] = st.text_area("Beneficiaries")
        details["assets"] = st.text_area("Assets")
    elif document_type == "Non-Disclosure Agreement (NDA)":
        details["disclosing_party"] = st.text_input("Disclosing Party")
        details["receiving_party"] = st.text_input("Receiving Party")
        details["nda_terms"] = st.text_area("NDA Terms")
    else:
        details["custom_details"] = st.text_area("Enter details for the custom document")

    if st.button("Generate Document"):
        pdf_url = draft_legal_document(document_type, details)

        if pdf_url:
            st.success("Document generated successfully!")
            st.markdown(f"[Download Enhanced Document from Generated Documents in backend](/{pdf_url})")
        else:
            st.error("Failed to generate the document.")
