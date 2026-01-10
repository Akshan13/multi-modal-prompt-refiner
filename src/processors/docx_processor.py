from docx import Document

def extract_docx_text(file_path):
        """Extract text from a DOCX file."""
        
        try:
            doc = Document(file_path)
            text = "\n".join([para.text for para in doc.paragraphs])
            return text.strip()
        except Exception as e:
            return f"Error extracting DOCX text: {e}"
      