def extract_text(file_path):  #    """Extracts text content from a given file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read().strip()  
        return text
    except Exception as e:
        print(f"Error: {e}")
        return ""  #  Always return str
