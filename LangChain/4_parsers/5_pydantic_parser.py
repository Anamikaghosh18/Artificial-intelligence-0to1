from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from pydantic import BaseModel, Field
from dotenv import load_dotenv 
import os 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser


load_dotenv()
api_key = os.getenv("HUGGINGFACE_ACCESS_TOKEN")


llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3.2-Exp",
    task="conversational",
    huggingfacehub_api_token=api_key
)


model = ChatHuggingFace(llm = llm)

class Person(BaseModel):
    name : str = Field(description="Name of the person")
    age : int = Field(gt = 18 , description="age of the person")
    city : str = Field(description="Name of the city the person belongs to")

parser = PydanticOutputParser(pydantic_object=Person)


# 1st prompt -> detailed report 
template1 = PromptTemplate(
    template = "Generate the name age and city of a fictional {place} person \n{format_instruction}", 
    input_variables=["place"], 
    partial_variables={"format_instruction" : parser.get_format_instructions()}
) 

chain = template1 | model | parser
respond = chain.invoke({"place" : "indian"}) # need to send something so blank dict bcz no input is there 
print(respond)


# you will get the json object but cant decide the schema that will be decided by the AI model 
