from fpdf import FPDF

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.add_page()
        self.set_font("Arial", size=12)

    def add_text(self, text):
        self.multi_cell(0, 10, text)

# Cria pdf
pdf = PDF()
ocr_text = "Este pdf foi gerado atraves de OCR."
ocr_img = r'C:\Users\DELL\Pictures\Saved Pictures\mwFzF.png'
pdf.add_text(ocr_text)
pdf.image(ocr_img)
pdf.output("scanned.pdf")