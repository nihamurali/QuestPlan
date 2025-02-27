from pypdf import PdfReader

def get_content(fpath):
    # creating a pdf reader object
    reader = PdfReader(fpath)
    contents = []
    # printing number of pages in pdf file
    
    page_cnt = len(reader.pages)
    print('No of Pages', page_cnt)
    for i in range(page_cnt):
        # getting a specific page from the pdf file
        page = reader.pages[i]
        # extracting text from page
        text = page.extract_text()
        #print(text)
        contents.append(text)
    return contents

#result = get_content('../../test.pdf')
#print(result)