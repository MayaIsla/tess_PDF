def get_pdf_searchable_pages(fname):
    # must have pdf miner (pip install pdfminer)
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
            print(f"Document '{fname}' has image based text. "
                  f"Complete document is non-searchable")
        elif len(non_searchable_pages) == 0:
            print(f"Document '{fname}' has embedded text. "
                  f"Complete document is searchable")
        else:
            print(f"searchable_pages : {searchable_pages}")
            print(f"non_searchable_pages : {non_searchable_pages}")
    else:
        print(f"Not a valid document")

if __name__ == '__main__':
     iO = input("Enter File Path: ")
     get_pdf_searchable_pages(iO)
