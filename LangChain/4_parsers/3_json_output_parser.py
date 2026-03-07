from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv 
import os 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser


load_dotenv()
api_key = os.getenv("HUGGINGFACE_ACCESS_TOKEN")


llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3.2-Exp",
    task="conversational",
    huggingfacehub_api_token=api_key
)


model = ChatHuggingFace(llm = llm)
parser = JsonOutputParser()


# 1st prompt -> detailed report 
template1 = PromptTemplate(
    template = "Give me the name , age , and city of a fictional person \n{format_instruction}", 
    input_variables=[], 
    partial_variables={"format_instruction" : parser.get_format_instructions()}
) 

chain = template1 | model | parser
respond = chain.invoke({}) # need to send something so blank dict bcz no input is there 
print(respond)


# you will get the json object but cant decide the schema that will be decided by the AI model 
