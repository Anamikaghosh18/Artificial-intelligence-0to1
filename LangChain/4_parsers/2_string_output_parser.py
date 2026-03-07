from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv 
import os 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()
api_key = os.getenv("HUGGINGFACE_ACCESS_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3.2-Exp",
    task="conversational",
    huggingfacehub_api_token=api_key
)

model = ChatHuggingFace(llm = llm)

# 1st prompt -> detailed report 
template1 = PromptTemplate(
    template= "Write a detailed report on {topic}", 
    input_variables=['topic']
) 

# 2nd prompt -> write a 5 lines summary 

template2= PromptTemplate(
    template="write a 5 lines summary on the following text . /n {text}", 
    input_variables=['text']
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

respond = chain.invoke({"topic" : "black hole"})

print(respond)





