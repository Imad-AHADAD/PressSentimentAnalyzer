from pytesseract import pytesseract
from PIL import Image

def extract_text_img(uploaded_img):
    image = Image.open(uploaded_img)
    # path vers tesseract OCR exe
    path_to_tesseract = r'RP_to_text\Ressources\Tesseract-OCR\tesseract.exe'
    pytesseract.tesseract_cmd = path_to_tesseract
    extracted_text = pytesseract.image_to_string(image, lang='eng')  # Apply OCR
   
    return extracted_text

