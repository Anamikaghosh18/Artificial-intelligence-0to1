from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from typing import Optional, Literal
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
class Review(BaseModel):
    summary: str = Field(description="A brief summary of the review")

    sentiment : Literal["pos", "neg"] = Field(description =  "Return sentiment of the review either negative , positive or neutral")

    name: Optional[str] = Field(default=None, description="Write the name of the reviewer")


structured_model = model.with_structured_output(Review)

respond = structured_model.invoke("""
                                  The hardware is great , but the software feels bloated . there are too many pre-installed apps that i cant remove . Also, the ui looks outdated compared to other brands . Hoping for a software update to fix this.
                                Review By- Anamika Ghosh                           
                                  """)

print(respond)

# typed dict
'''
class Person(TypedDict):
    name : str 
    age : int

new_person: Person = {"name":"Anamika", "age":20}

'''

