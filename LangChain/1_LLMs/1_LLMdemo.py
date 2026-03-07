import os 
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv('GEMINI_API_KEY')
llm = GoogleGenerativeAI(
    model = 'gemini-2.5-flash',
    google_api_key = api_key)

respond = llm.invoke("what is the capital of india")
print(respond)