# import os
# from app.utils.pdf_generator import create_pdf

# TEMPLATES = {
#     "Contract": "This contract is made between {party_one} and {party_two}. Terms: {contract_terms}",
#     "Will": "This is the last will of {testator_name}. Beneficiaries: {beneficiaries}. Assets: {assets}",
#     "Non-Disclosure Agreement (NDA)": "This NDA is between {disclosing_party} and {receiving_party}. Terms: {nda_terms}",
# }

# def generate_legal_document(document_type: str, details: dict) -> str:
#     """
#     Generate a legal document based on the document type and user-provided details.
    
#     Args:
#         document_type (str): Type of document (Contract, Will, NDA, etc.)
#         details (dict): User-provided details (name, terms, etc.)

#     Returns:
#         str: Path to the generated PDF document.
#     """
#     if document_type not in TEMPLATES:
#         raise ValueError("Unsupported document type.")

#     # Fill the template with user-provided details
#     document_text = TEMPLATES[document_type].format(**details)
    
#     # Generate a PDF
#     pdf_filename = f"{document_type.replace(' ', '_').lower()}.pdf"
#     pdf_path = os.path.join("generated_documents", pdf_filename)

#     create_pdf(document_text, pdf_path)

#     return pdf_path

import os
import requests
from app.utils.pdf_generator import create_pdf

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

TEMPLATES = {
    "Contract": "This contract is made between {party_one} and {party_two}. Terms: {contract_terms}",
    "Will": "This is the last will of {testator_name}. Beneficiaries: {beneficiaries}. Assets: {assets}",
    "Non-Disclosure Agreement (NDA)": "This NDA is between {disclosing_party} and {receiving_party}. Terms: {nda_terms}",
}

def enhance_with_gemini(text: str) -> str:
    """
    Sends the legal document draft to Gemini API for improved wording.

    Args:
        text (str): Raw legal document draft.

    Returns:
        str: Enhanced legal document.
    """
    if not GEMINI_API_KEY:
        return "Error: Missing Gemini API Key."

    payload = {"contents": [{"parts": [{"text": f"Refine and enhance this legal document:\n{text}"}]}]}
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(GEMINI_API_URL, json=payload, headers=headers)
        response.raise_for_status()
        result = response.json()

        if "candidates" in result and result["candidates"]:
            return result["candidates"][0].get("content", {}).get("parts", [{}])[0].get("text", "No response.")
        return "No valid response from API."

    except requests.exceptions.RequestException as e:
        return f"Error: Failed to connect to Gemini API - {str(e)}"
    except KeyError:
        return "Error: Unexpected API response format."

def generate_legal_document(document_type: str, details: dict) -> str:
    """
    Generate a legal document, enhance it with Gemini, and return a PDF.

    Args:
        document_type (str): Type of document (Contract, Will, NDA, etc.)
        details (dict): User-provided details (name, terms, etc.)

    Returns:
        str: Path to the generated PDF document.
    """
    if document_type not in TEMPLATES:
        raise ValueError("Unsupported document type.")

    # Fill template with user inputs
    raw_document = TEMPLATES[document_type].format(**details)

    # Send to Gemini for wording improvement
    refined_document = enhance_with_gemini(raw_document)

    # Generate PDF with refined text
    pdf_filename = f"{document_type.replace(' ', '_').lower()}.pdf"
    pdf_path = os.path.join("generated_documents", pdf_filename)
    create_pdf(refined_document, pdf_path)

    return pdf_path
