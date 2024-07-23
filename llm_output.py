import langchain_google_genai
import getpass
import configparser
import os
from langchain_google_genai import ChatGoogleGenerativeAI

class Llm_caller:
    def __init__(self) -> None:
        config = configparser.ConfigParser()
        config.read('config.ini')
        os.environ['GOOGLE_API_KEY'] = config.get('API','gemini_api')

    def initiate_model(self):
        print("Initiating model......")
        llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-pro",
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2,
        )
        return llm
    
    def create_prompt(self,resume_data):
        messages = [
            (
                "system",
                """You are a resume creator. Create a resume from the user data based on following order Name,
                 professional experience, technical skills, software skills, project details, academic details. 
                Please remove all the other details. If any details above mentioned are not available,
                 donot answer the question yourself. Provide '#{name}' for name, '##{heading}' for main heading and '###{heading}' for subheading.
                 Avoid unwanted '#' in the prompt""",
            ),
            ("human", resume_data),
        ]
        return messages
    
    def send_api_req(self,resume_data):
        llm_model = self.initiate_model()
        prompt = self.create_prompt(resume_data)
        print("Send API to LLM........")
        ai_msg = llm_model.invoke(prompt)
        return ai_msg.content
