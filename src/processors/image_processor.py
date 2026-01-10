import easyocr 

def extract_image_text(file_path):
    """"Extract text from an image file using EasyOCR."""
    try:
        #Intialize EasyOCR reader
        reader = easyocr.Reader(['en'],gpu=False)

        #Extract text from image        
        result = reader.readtext(file_path)
    
    #result = [(bbox, text, confidence), ...]
        #Get only the text parts
        text = " ".join([detection[1] for detection in result])
        
        return text.strip()
    except Exception as e:
        return f"Error extracting image text: {e}"
