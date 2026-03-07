from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os 

# Load .env variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Initialize embeddings
embedding = GoogleGenerativeAIEmbeddings(
    model='gemini-embedding-001',
    api_key=api_key  # correct parameter name
)

# Generate embedding
respond = embedding.embed_query("hey i am anamika")

print(respond)
