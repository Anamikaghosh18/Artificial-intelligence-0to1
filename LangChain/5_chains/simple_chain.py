from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
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

prompt = PromptTemplate(
    template = "Generate 5 intersting facts about {topic}", 
    input_variables=["topic"]
)

model = ChatHuggingFace(llm = llm)

parser = StrOutputParser()

# lanchain expressing language 
chain = prompt | model | parser 

respond = model.invoke({"topic": "cricket"}); 

print(respond); 

