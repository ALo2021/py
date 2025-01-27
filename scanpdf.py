import pytesseract
import re
from pdf2image import convert_from_path

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

images = convert_from_path("C:\setup\py\scanned.pdf")

for i, image in enumerate(images): 
    text = pytesseract.image_to_string(image)
    emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    print(f"Page {i + 1} Emails: {emails}")
