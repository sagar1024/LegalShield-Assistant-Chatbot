def generate_legal_document(document_type: str, details: dict) -> str:
    templates = {
        "contract": """
        Contract Agreement

        Between: {party_one} and {party_two}

        Terms and Conditions:
        {terms}

        Signed:
        ______________________ (Party 1)
        ______________________ (Party 2)
        """,
        "nda": """
        Non-Disclosure Agreement (NDA)

        This agreement is between {disclosing_party} and {receiving_party}.
        
        Confidential Information:
        {confidential_info}

        Signed:
        ______________________ (Disclosing Party)
        ______________________ (Receiving Party)
        """,
    }

    template = templates.get(document_type.lower(), "Invalid document type.")
    
    return template.format(**details) if template != "Invalid document type." else template
