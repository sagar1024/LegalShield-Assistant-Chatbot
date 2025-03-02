import numpy as np
import re
import cv2
import fitz  #PyMuPDF for PDF processing
import io
import pytesseract
from PIL import Image
from fastapi import UploadFile
from app.utils.external_api import call_gemini_api

async def process_document(file: io.BytesIO, summary_length: int, focus_sections: str, language: str):
    """
    Process the uploaded document to extract text.
    """
    text_content = ""
    pdf_document = fitz.open(stream=file.read(), filetype="pdf")
    for page in pdf_document:
        text_content += page.get_text("text") + "\n"

    #Generate summary
    summary = await summarize_text(text_content, summary_length, language)

    return {
        "summary": summary
    }

async def summarize_text(text: str, summary_length: int, language: str) -> str:
    """
    Uses the Gemini API to analyze the document text and generate a summary.
    Handles long texts by processing in chunks.
    """
    chunk_size = 5000
    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
    summaries = [
        await call_gemini_api(f"Summarize the following document in {language}. Keep it approximately {summary_length} words:\n\n{chunk}")
        for chunk in chunks
    ]
    return "\n".join(summaries)

#HELPER functions -

#This filter function is over killing
#Need a more subtle technique for filtering section
def filter_focus_sections(text: str, focus_sections: str) -> str:
    """
    Filters the document text based on the provided focus sections.
    """
    sections = focus_sections.split(",")
    filtered_text = ""

    for section in sections:
        section = section.strip()
        pattern = rf"{section}.*?(?=\n[A-Z])"
        matches = re.findall(pattern, text, re.DOTALL)

        if matches:
            filtered_text += " ".join(matches) + "\n"

    return filtered_text if filtered_text else text

def clean_extracted_text(text):
    # Remove non-ASCII characters
    cleaned_text = re.sub(r'[^\x00-\x7F]+', ' ', text)
    
    # Remove extra whitespace
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    
    return cleaned_text
