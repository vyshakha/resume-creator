from pdfminer.high_level import extract_text as pdfminer_extract_text
import io
import requests

class Pdf_reader:
    def __init__(self) -> None:
        pass
    
    def get_pdf_text_from_url(self,urls):
        print("Reading pdf from given URL........")
        text = ""
        for url in urls:
            response = requests.get(url)
            pdf_file = io.BytesIO(response.content)
            text += pdfminer_extract_text(pdf_file)
        return text
    
