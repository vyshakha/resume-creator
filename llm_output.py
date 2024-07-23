import langchain_google_genai
import getpass
import configparser
import os

class Llm_caller:
    def __init__(self) -> None:
        config = configparser.ConfigParser()
        config.read('config.ini')
        os.environ['GOOGLE_API_KEY'] = config.get('API','gemini_api')


cl = Llm_caller()
        