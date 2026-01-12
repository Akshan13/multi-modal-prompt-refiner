import os 
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

from processors.text_processor import extract_text
from processors.pdf_processor import extract_pdf_text
from processors.docx_processor import extract_docx_text
from processors.image_processor import extract_image_text
from refiner.llm_refiner import refine_with_llm
from refiner.template import RefinedPrompt


def refine_multimodal(
    text_path: str = None,
    pdf_path: str = None,
    docx_path: str = None,
    image_path: str = None
) -> RefinedPrompt:
    """
    Accepts multiple input types and combines them for unified refinement.
    
    Args:
        text_path: Path to .txt file
        pdf_path: Path to .pdf file
        docx_path: Path to .docx file
        image_path: Path to image file (.png, .jpg)
    
    Returns:
        RefinedPrompt: Structured prompt with combined information
    """
    
    combined_text = ""
    sources_used = []
    
    # Extract from all provided sources
    if text_path and os.path.exists(text_path):
        print(f"📝 Extracting from text: {text_path}")
        text_content = extract_text(text_path)
        print(f"   Length: {len(text_content)} chars")
        if text_content and not text_content.startswith("Error"):
            combined_text += f"\n--- From Text File ---\n{text_content}\n"
            sources_used.append("text_file")
    
    if pdf_path and os.path.exists(pdf_path):
        print(f" Extracting from PDF: {pdf_path}")
        pdf_content = extract_pdf_text(pdf_path)
        print(f"   Length: {len(pdf_content)} chars")
        print(f"   Content: {pdf_content[:200]}")  
        if pdf_content and not pdf_content.startswith("Error"):
            combined_text += f"\n--- From PDF Document ---\n{pdf_content}\n"
            sources_used.append("pdf")
    
    if docx_path and os.path.exists(docx_path):
        print(f" Extracting from DOCX: {docx_path}")
        docx_content = extract_docx_text(docx_path)
        print(f"   Length: {len(docx_content)} chars")
        if docx_content and not docx_content.startswith("Error"):
            combined_text += f"\n--- From Word Document ---\n{docx_content}\n"
            sources_used.append("docx")
    
    if image_path and os.path.exists(image_path):
        print(f"Extracting from Image: {image_path}")
        image_content = extract_image_text(image_path)
        print(f"   Length: {len(image_content)} chars")
        print(f"   Content: {image_content[:200]}")  
        if image_content and len(image_content.strip()) > 10:
            combined_text += f"\n--- From Image (OCR) ---\n{image_content}\n"
            sources_used.append("image")
    
    # Validation
    if not combined_text.strip():
        raise ValueError("No valid content extracted from any source!")
    
    print(f"\nSources used: {', '.join(sources_used)}")
    print(f" Combined text length: {len(combined_text)} characters\n")
    
    # DEBUG: Show what we're sending to LLM
    print("\n" + "="*70)
    print("COMBINED TEXT BEING SENT TO LLM:")
    print("="*70)
    print(combined_text)
    print("="*70 + "\n")

    # Refine combined content with LLM
    try:
        refined = refine_with_llm(combined_text)
        return refined
    except Exception as e:
        print(f"\n LLM Refinement Failed!")
        print(f"Error: {e}")
        raise
