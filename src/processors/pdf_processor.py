import fitz  # PyMuPDF


def extract_pdf_text(file_path):
    """Extract text from a PDF file using PyMuPDF."""
    try:  # ✅ Indented 4 spaces from def
        doc = fitz.open(file_path)
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        return text.strip()
    except Exception as e:  # ✅ Same level as try
        return f"Error extracting PDF text: {e}"

