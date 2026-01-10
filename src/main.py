import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#Processors
from processors.text_processor import extract_text
from processors.pdf_processor import extract_pdf_text
from processors.docx_processor import extract_docx_text
from processors.image_processor import extract_image_text

#Refiner
from refiner.extractor import refine_text_to_prompt


# Processor TESTING
# #TEXT TESTING
if __name__ == "__main__":
    text = extract_text("data/samples/text_samples.txt")
    print("TEXT EXTRACTED:", text)

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
print("\n" + "="*50)
print("REFINING TEXT TO STRUCTURED PROMPT:")
print("="*50)

refined = refine_text_to_prompt(text)  # Use text from text_processor
print(refined.model_dump_json(indent=2))