import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

load_dotenv()
api_key = os.getenv('HUGGINGFACE_ACCESS_TOKEN')

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3.2-Exp",
    task="conversational",
    huggingfacehub_api_token=api_key
)

model = ChatHuggingFace(llm = llm)

response = model.invoke("What is the capital of India?")
print(response.content)
