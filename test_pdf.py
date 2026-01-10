import fitz

pdf_path = r"D:\Projects\multi-modal-prompt-refiner\data\samples\sample.pdf"

try:
    print(f"Attempting to open: {pdf_path}")
    doc = fitz.open(pdf_path)
    print(f"✅ Success! Pages: {doc.page_count}")
    
    for i, page in enumerate(doc):
        text = page.get_text()
        print(f"\nPage {i+1} text ({len(text)} chars):")
        print(text[:200])
    
    doc.close()
except Exception as e:
    print(f"❌ Error: {type(e).__name__}")
    print(f"Details: {e}")
