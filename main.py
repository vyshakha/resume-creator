from llm_output import Llm_caller
from pdf_reader import Pdf_reader

call_module = Llm_caller()
pd = Pdf_reader()

res_urls = [
    "https://leadsochrms.s3.amazonaws.com/Resume/1706012040697",
    "https://leadsochrms.s3.amazonaws.com/Resume/1706007937038",
    "https://leadsochrms.s3.amazonaws.com/Resume/1706001080833",
    "https://leadsochrms.s3.amazonaws.com/Resume/1705992109383",
    "https://leadsochrms.s3.amazonaws.com/Resume/1705986064821",
    "https://leadsochrms.s3.amazonaws.com/Resume/1705918983470",
    "https://leadsochrms.s3.amazonaws.com/Resume/1705916738904",
    "https://leadsochrms.s3.amazonaws.com/Resume/1705913042386",
    "https://leadsochrms.s3.amazonaws.com/Resume/1705910746093",
    "https://leadsochrms.s3.amazonaws.com/Resume/1705900253540",
    "https://leadsochrms.s3.amazonaws.com/Resume/1705651101041",
    "https://leadsochrms.s3.amazonaws.com/Resume/1705644901531",
    "https://leadsochrms.s3.amazonaws.com/Resume/1705582283897"
]

for index,each_resume in enumerate(res_urls):
    print("*"*50)
    print(f"Starting {index+1} out of {len(res_urls)}")
    res_data = pd.get_pdf_text_from_url(each_resume)
    if res_data:
        pdf_data = call_module.send_api_req(res_data)
        with open(f'./txt_outputs/{index+1}.txt','w+') as f:
            f.write(pdf_data)
    print(f"Completed {index+1} out of {len(res_urls)}")