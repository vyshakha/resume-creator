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
        llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-pro",
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2,
        )
        return llm
    
    def create_prompt(self):
        messages = [
            (
                "system",
                "You are a helpful assistant that translates English to French. Translate the user sentence.",
            ),
            ("human", "I love programming."),
        ]
        return messages
    
    def send_api_req(self):
        llm_model = self.initiate_model()
        prompt = self.create_prompt()
        ai_msg = llm_model.invoke(prompt)
        return ai_msg.content


cl = Llm_caller()
        