import sys
import logging
import os
import errno

LOG_FILENAME = 'C:/DIR/to/log/new.log'    
logging.getLogger('PIL').setLevel(logging.WARNING)

def get_PIC():
    from PIL import Image
    from pdf2image import convert_from_path
    from pytesseract import image_to_string
    from pytesseract import pytesseract
    import os
    
    logging.debug('I am the culprit!')
    converted_scan = convert_from_path(iO ,100,poppler_path='C:/dir/to/Poppler/poppler-23.05.0/Library/bin')
    #converted_scan = convert_from_path(iO)
    #for entry in os.scandir()
    
   
    logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
    
    logging.debug('Here')
    
    basename = os.path.splitext(os.path.basename(iO))[0]
    dirc = "C:/dir/to/pdf/" +basename+ "/"
    dirc3 = "C:/dir/to/pdf/" +basename

    try:
        os.makedirs(dirc)
        dirc2 = [os.path.join(dirc3, f) for f in os.listdir(dirc3) if os.path.isfile(os.path.join(dirc3, f))]
    except OSError as e:
        if e.errno == errno.EEXIST:
            print('Directory not created.')
        else:
            raise
        
    
    

    pytesseract.tesseract_cmd = 'C:/dir/to/Tesseract/tesseract.exe' #path to tesseract 

    for i, image  in enumerate(converted_scan):
        fname = dirc + basename +str(i) +".png"
        print(fname)
        logging.debug('Im ded')
        image.save(fname, "PNG")

def get_OCR():

    from PIL import Image
    from pdf2image import convert_from_path
    from pytesseract import image_to_string
    from pytesseract import pytesseract
    import os
    
    #converted_scan = convert_from_path(iO ,100,poppler_path='C:/dir/to/Poppler/poppler-23.05.0/Library/bin')
    #converted_scan = convert_from_path(iO)
    #for entry in os.scandir()

    basename = os.path.splitext(os.path.basename(iO))[0]
    logging.debug('Creating folder...')
    dirc = "C:/dir/to/pdf/" +basename+ "/"
    dirc3 = "C:/dir/to/pdf/" +basename

    dirc2 = [os.path.join(dirc3, f) for f in os.listdir(dirc3) if os.path.isfile(os.path.join(dirc3, f))]
    pytesseract.tesseract_cmd = 'C:/dir/to/Tesseract/tesseract.exe' #path to tesseract 
    
    for j, file in enumerate(dirc2):
        logging.debug('Exporting files...')
        print("File # " + str(j) + " is being processed...")
        fname = dirc + basename + str(j) + ".png"
        text = image_to_string(Image.open(fname))
        with open(file + ".txt", 'w') as outfile:
                outfile.write(text)

def garbage_collection():

    basename = os.path.splitext(os.path.basename(iO))[0]
    dirc = "C:/dir/to/pdf/" +basename+ "/"
    dirc3 = "C:/dir/to/pdf/" +basename
    dirc2 = [os.path.join(dirc3, f) for f in os.listdir(dirc3) if os.path.isfile(os.path.join(dirc3, f))]
    
    createdDir = os.listdir(dirc)
    
    for item in createdDir:
        if item.endswith(".png"):
            os.remove(os.path.join(dirc3, item))
    




if __name__ == '__main__':
  iO = (sys.argv[1]) # so you can CLI verify_PDF.py "DIR to PDF (must be in quotes for white spaces..)"
  print("Code Starting...")
  get_PIC()
  print("Exporting OCR..")
  get_OCR()
  print("Cleaning up...")
  garbage_collection()
  
  
