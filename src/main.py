import sys
import os
import warnings
warnings.filterwarnings('ignore', category=FutureWarning)

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#Processors
from processors.text_processor import extract_text
from processors.pdf_processor import extract_pdf_text
from processors.docx_processor import extract_docx_text
from processors.image_processor import extract_image_text

#Refiners
from refiner.extractor import refine_text_to_prompt
#LLM Refiner
from refiner.llm_refiner import refine_with_llm
#Multi-Modal Refiner
from src.refiner.multi_modal_refiner import refine_multimodal



# Processor TESTING
# #TEXT TESTING
# if __name__ == "__main__":
#     text = extract_text("data/samples/text_samples.txt")
#     print("TEXT EXTRACTED:", text)

# #PDF TESTING
# print("\n--- PDF TESTING ---")
# pdf_text = extract_pdf_text("data/samples/sample.pdf")
# print("PDF TEXT EXTRACTED:", pdf_text)


# #docx TESTING
# docx_text = extract_docx_text("data/samples/sample.docx")
# print("\n--- DOCX TESTING ---")
# print("DOCX TEXT EXTRACTED:", docx_text)


#image TESTING
# if __name__ == "__main__":
#     print("\n--- IMAGE TESTING ---")
#     image_text = extract_image_text("data/samples/sample.png")
#     print("IMAGE TEXT EXTRACTED:", image_text)
    
    
#Refiner TESTING
# print("\n" + "="*50)
# print("REFINING TEXT TO STRUCTURED PROMPT:")
# print("="*50)

# refined = refine_text_to_prompt(text)  # Use text from text_processor
# print(refined.model_dump_json(indent=2))

#LLM Refiner TESTING for TEXT
# if __name__ == "__main__":
#     print("\n" + "="*50)
#     print("REFINING TEXT WITH Gemini:")
#     print("="*50)
    
#     refined = refine_with_llm(text)
#     print(refined.model_dump_json(indent=2))
    
#     # Test rejection
#     print("\n--- REJECTION TEST ---")
#     try:
#         invalid = refine_with_llm("Random gibberish hello world")
#     except ValueError as e:
#         print(f"Correctly rejected: {e}")
        
#LLM Refiner TESTING for PDF
# if __name__ == "__main__":
#     # PDF EXTRACTION DEBUG
#     print("="*50)
#     print("PDF EXTRACTION TEST:")
#     print("="*50)
    
#     pdf_text = extract_pdf_text("data/samples/sample.pdf")
    
#     # DEBUG: Show what was extracted
#     print(f"\nExtracted Text Length: {len(pdf_text)} characters")
#     print(f"\nFirst 500 characters:")
#     print(pdf_text[:500])
#     print(f"\nFull Content:")
#     print(pdf_text)
#     print("\n" + "="*50)
    
#     # Only refine if extraction worked
#     if len(pdf_text.strip()) > 20 and not pdf_text.startswith("Error"):
#         print("\nREFINING PDF TEXT WITH Gemini:")
#         print("="*50)
        
#         refined_pdf = refine_with_llm(pdf_text)
#         print(refined_pdf.model_dump_json(indent=2))
#     else:
#         print(f"PDF extraction failed or text too short!")
#         print(f"Content: '{pdf_text}'")

#LLM Refiner TESTING for DOCX
# if __name__ == "__main__":
#     # DOCX EXTRACTION TEST
#     print("="*50)
#     print("DOCX EXTRACTION TEST:")
#     print("="*50)
    
#     docx_text = extract_docx_text("data/samples/sample.docx")
    
#     print(f"\n Extracted Text Length: {len(docx_text)} characters")
#     print(f"\n Content:")
#     print(docx_text)
#     print("\n" + "="*50)
    
#     if len(docx_text.strip()) > 20 and not docx_text.startswith("Error"):
#         print("\nREFINING DOCX TEXT WITH Gemini:")
#         print("="*50)
        
#         refined_docx = refine_with_llm(docx_text)
#         print(refined_docx.model_dump_json(indent=2))
#     else:
#         print(f"DOCX extraction failed!")

#LLM Refiner TESTING for IMAGE
# if __name__ == "__main__":
#     # IMAGE OCR EXTRACTION TEST
#     print("="*50)
#     print("IMAGE OCR EXTRACTION TEST:")
#     print("="*50)
    
#     image_text = extract_image_text("data/samples/sample.jpeg")
    
#     print(f"\nExtracted Text Length: {len(image_text)} characters")
#     print(f"\nContent:")
#     print(image_text)
#     print("\n" + "="*50)
    
#     if len(image_text.strip()) > 20:
#         print("\nREFINING IMAGE TEXT WITH Gemini:")
#         print("="*50)
        
#         refined_image = refine_with_llm(image_text)
#         print(refined_image.model_dump_json(indent=2))
#     else:
#         print(f"Image OCR failed or no text found!")

#Multi-Modal Refiner TESTING
# if __name__ == "__main__":
#     print("="*70)
#     print("MULTI-MODAL REFINEMENT TEST")
#     print("="*70)
    
#     # Test 1: Single source (text only)
#     print("\nTEST 1: Text Only")
#     print("-"*70)
#     result1 = refine_multimodal(text_path="data/samples/text_samples.txt")
#     print(result1.model_dump_json(indent=2))
    
#     # Test 2: PDF + Image combined
#     print("\n\nTEST 2: PDF + Image Combined")
#     print("-"*70)
#     result2 = refine_multimodal(
#         pdf_path="data/samples/sample.pdf",
#         image_path="data/samples/sample.jpeg"
#     )
#     print(result2.model_dump_json(indent=2))
    
#     # Test 3: ALL formats combined
#     print("\n\nTEST 3: ALL Formats Combined")
#     print("-"*70)
#     result3 = refine_multimodal(
#         text_path="data/samples/text_samples.txt",
#         pdf_path="data/samples/sample.pdf",
#         docx_path="data/samples/sample.docx",
#         image_path="data/samples/sample.jpeg"
#     )
#     print(result3.model_dump_json(indent=2))