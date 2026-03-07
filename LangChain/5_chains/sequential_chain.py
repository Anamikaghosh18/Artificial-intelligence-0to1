from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

from langchain.chains import LLMChain, SequentialChain
import os 
from dotenv import load_dotenv 
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

parser = StrOutputParser()


prompt1 = PromptTemplate(
    template = "Generate a detailed report about {topic}", 
    input_variables=["topic"]
)
chain1 = LLMChain(
    llm = model , 
    prompt = prompt1, 
    output_parser = parser , 
    verbose = True, 
    output_key = "text",
)

prompt2 = PromptTemplate(
    template= "Generate a 5 lines summary on the given text \n {text}", 
    input_variables= ["text"]

)

chain2 = LLMChain(
    llm = model , 
    prompt = prompt2, 
    output_parser = parser , 
    verbose = True, 
    output_key = "summary"
)


# lanchain expressing language 
result_chain = SequentialChain(
    chains=[chain1, chain2],
    input_variables=["topic"],
    output_variables=["summary"],  # final output
    verbose=True
)

response = result_chain.invoke({"topic": "cricket"})
print(response)

