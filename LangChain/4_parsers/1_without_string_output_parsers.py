from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv 
import os 
from langchain_core.prompts import PromptTemplate

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


prompt1 = template1.invoke({"topic":"black hole"})

result1 = model.invoke(prompt1)

prompt2 = template2.invoke({"text": result1.content})

result2 = model.invoke(prompt2)

print(result2.content)