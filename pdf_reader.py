from pdfminer.high_level import extract_text as pdfminer_extract_text
import io
import requests

class Pdf_reader:
    def __init__(self) -> None:
        pass
    
    def get_pdf_text_from_url(self,url):
        print("Reading pdf from given URL........")
        try:
            response = requests.get(url)
            pdf_file = io.BytesIO(response.content)
            return pdfminer_extract_text(pdf_file)
        except:
            print(f"Unexpected document {url}")
            return None
        
    
