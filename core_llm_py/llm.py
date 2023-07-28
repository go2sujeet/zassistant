# return llm instance
from langchain.llms import OpenAI;
import os
# read the api key from the environment
def get_llm():
    return OpenAI(openai_api_key=os.environ["OPENAI_API_KEY"])



