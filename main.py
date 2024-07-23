from llm_output import Llm_caller
from pdf_reader import Pdf_reader

call_module = Llm_caller()
pd = Pdf_reader()

input_data = pd.get_pdf_text_from_url(['https://leadsochrms.s3.amazonaws.com/Resume/1706012040697'])

pdf_data = call_module.send_api_req(input_data)

print(pdf_data)