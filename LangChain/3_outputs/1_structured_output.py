from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from typing import TypedDict, Annotated
from dotenv import load_dotenv
import os 


load_dotenv()
api_key = os.getenv("HUGGINGFACE_ACCESS_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3.2-Exp",
    task="conversational",
    huggingfacehub_api_token=api_key
)

model = ChatHuggingFace(llm = llm)

# schema 
class Review(TypedDict):
    summary: Annotated[str, "A brief summary of the review"] 
    sentiment : Annotated[str, "Return sentiment of the review either negative , positive or neutral"] 

structured_model = model.with_structured_output(Review)

respond = structured_model.invoke("""The hardware is great , but the software feels bloated . there are too many pre-installed apps that i cant remove . Also, the ui looks outdated compared to other brands . Hoping for a software update to fix this.""")

print(respond)

# typed dict
'''
class Person(TypedDict):
    name : str 
    age : int

new_person: Person = {"name":"Anamika", "age":20}

'''

