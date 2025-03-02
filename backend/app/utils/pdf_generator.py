from fpdf import FPDF
import os

def create_pdf(content: str, filename: str):
    """
    Generates a PDF with given text content.

    Args:
        content (str): The text content to include in the PDF.
        filename (str): The filename to save the PDF.
    """
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.multi_cell(0, 10, content)

    os.makedirs(os.path.dirname(filename), exist_ok=True)
    pdf.output(filename)
