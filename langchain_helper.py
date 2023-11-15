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
    #Chain 1: Restaurant Name 
    prompt_template_name = PromptTemplate(
        input_variables = ['cusine'],
        template = 'I want to open a restaurant for {cusine} food. Suggest a name for the restaurant.'
    )

    name_chain = LLMChain(llm=llm, prompt = prompt_template_name, output_key= 'restaurant_name')

    #Chain 2 : Menu Items
    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template = 'Suggest some menu items for the {restaurant_name}.Return the items with comma seperated string.'
    )

    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key='menu_items')

    chain = SequentialChain(
        chains = [name_chain, food_items_chain],
        input_variables= ['cusine'],
        output_variables= ['restaurant_name', 'menu_items']
    )

    response = chain({'cusine': cusine})

    return response 


if __name__ == "__main__":
    print(generate_restaurant_name_and_items("Italian"))
