from PyPDF2 import PdfReader

def parse_resume(path):
    reader=PdfReader(path)
    text=''
    for p in reader.pages:
        text+=p.extract_text()
    return text.lower()
