import streamlit as st

def show():
    st.title("Legal Document Drafting")

    # Dropdown for selecting the document type
    document_type = st.selectbox("Select a document type", ["Contract", "Will", "Non-Disclosure Agreement (NDA)", "Other"])

    st.write(f"You selected: {document_type}")

    # Define the input fields for each document type
    if document_type == "Contract":
        st.subheader("Contract Details")
        contract_name = st.text_input("Contract Name")
        party_one = st.text_input("Party 1 (Name or Organization)")
        party_two = st.text_input("Party 2 (Name or Organization)")
        contract_terms = st.text_area("Contract Terms")

        if st.button("Generate Contract"):
            # Placeholder for actual contract generation logic
            st.write(f"Contract '{contract_name}' between {party_one} and {party_two}.")
            st.write(f"Terms: {contract_terms}")

    elif document_type == "Will":
        st.subheader("Will Details")
        testator_name = st.text_input("Testator's Name")
        beneficiaries = st.text_area("Beneficiaries (List them)")
        assets = st.text_area("Assets to be Distributed")

        if st.button("Generate Will"):
            # Placeholder for actual will generation logic
            st.write(f"Will for {testator_name}.")
            st.write(f"Beneficiaries: {beneficiaries}")
            st.write(f"Assets: {assets}")

    elif document_type == "Non-Disclosure Agreement (NDA)":
        st.subheader("NDA Details")
        disclosing_party = st.text_input("Disclosing Party")
        receiving_party = st.text_input("Receiving Party")
        nda_terms = st.text_area("NDA Terms")

        if st.button("Generate NDA"):
            # Placeholder for actual NDA generation logic
            st.write(f"NDA between {disclosing_party} and {receiving_party}.")
            st.write(f"Terms: {nda_terms}")

    else:
        st.subheader("Custom Legal Document")
        custom_details = st.text_area("Enter the details of your document")

        if st.button("Generate Document"):
            # Placeholder for custom document generation logic
            st.write(f"Custom Document: {custom_details}")
            