from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain.chains import SequentialChain
from secret_key import openapi_key

import os 
os.environ['OPENAI_API_KEY'] = openapi_key

llm = OpenAI(temperature = 0.7)


def generate_restaurant_name_and_items(cusine):
    return {
        'restaurant_name' : 
    }