from PIL import Image
from pdf2image import convert_from_path
from pytesseract import image_to_string
from pytesseract import pytesseract

converted_scan = convert_from_path('scanned.pdf', 500, poppler_path=r'D:\Desktop\poppler\bin')

for i in converted_scan:
    i.save('scan_image.png', 'png')

pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
text = image_to_string(Image.open('scan_image.png'))
with open('scan_text_output.txt', 'w') as outfile:
    outfile.write(text.replace('\n\n', '\n'))

# prereqs are to install poppler via github, and import pytesseract packages directly
# must have txt file, sample pdf (named scanned.pdf in this example), and lots of sheer luck.
# Scares me how it parces txt files so well....
