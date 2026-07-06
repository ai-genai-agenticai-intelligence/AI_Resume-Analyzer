from PyPDF2 import PdfReader

def extract_text(file_path):
    reader = PdfReader(file_path)
    text = ""  # Fixed typo here

    for page in reader.pages:
        page_text = page.extract_text()  # Extracted text into a variable
        if page_text:
            text += page_text
            
    return text  # Moved outside the loop to read all pages
