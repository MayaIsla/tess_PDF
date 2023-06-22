import importsConfig as cfg
out = "" #initialize output variable

def get_pdf_searchable_pages(fname):
    from pdfminer.pdfpage import PDFPage
    searchable_pages = []
    non_searchable_pages = []
    page_num = 0


    with open(fname, 'rb') as infile:

        for page in PDFPage.get_pages(infile):
            page_num += 1
            if 'Font' in page.resources.keys():
                searchable_pages.append(page_num)
            else:
                non_searchable_pages.append(page_num)
    if page_num > 0:
        if len(searchable_pages) == 0:
            global out #makes output variable global for all classes to use.
            out = "no"
            print(out)
            return out
            
        elif len(non_searchable_pages) == 0:
            out = "yes"
            print(out)
            return out
    else:
        out = "invalid"
        print(out)
        return out


def get_OCR():
    from PIL import Image
    from pdf2image import convert_from_path
    from pytesseract import image_to_string
    from pytesseract import pytesseract
    converted_scan = convert_from_path(iO ,500,poppler_path='C:/path/to/poppler/bin/folder/bin')
    
    for i in converted_scan:
        i.save(r'C:\\path\\to\\image_file.png', 'png') #path to saved image

    pytesseract.tesseract_cmd = r'C:\\path\\to\\tesseract\\executable\\tesseract.exe' #path to tesseract
    text = image_to_string(Image.open(r'C:\\path\\to\\image_file.png')) #path to the png file created previously.
    with open(r'C:\\path\\to\\text_file.txt', 'w') as outfile: #path to the txt file.
        outfile.write(text.replace('\n\n', '\n'))


def scrape_Text():
    import tika
    from tika import parser

    file = parser.from_file(iO)
    outout = file['content']
    outout = outout.encode('ascii', errors='ignore')
    with open(r'C:\\path\\to\\text_file.txt', 'w') as fileout: #path to the txt file.
        fileout.write(str(outout))



if __name__ == '__main__':
     iO = input("Enter File Path: ")
     get_pdf_searchable_pages(iO)
     if out == "no" : get_OCR() #if the pdf is scanned, it will scan for you
     else: scrape_Text() #otherwise scrape text from pdf.


