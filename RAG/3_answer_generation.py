import os
from dotenv import load_dotenv

from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.chat_models import ChatHuggingFace
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
persist_directory = os.path.join(BASE_DIR, "db", "chroma_db")

# Embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)

# Load vector DB
db = Chroma(
    persist_directory=persist_directory,
    embedding_function=embeddings,
    collection_metadata={"hnsw:space": "cosine"}
)

# Query
query = "How much did Microsoft pay to acquire GitHub?"

retriever = db.as_retriever(search_kwargs={"k": 5})
relevant_docs = retriever.invoke(query)

print(f"User Query: {query}")
print("--- Context ---")

for i, doc in enumerate(relevant_docs, 1):
    print(f"Document {i}:\n{doc.page_content}\n")

# Combine context
combined_input = f"""Based on the following documents, please answer this question: {query}

Documents:
{chr(10).join([f"- {doc.page_content}" for doc in relevant_docs])}

If the answer is not in the documents, say:
"I don't have enough information to answer that question based on the provided documents."
"""

# LLM
model = ChatHuggingFace(model="nvidia/Nemotron-Cascade-2-30B-A3B")

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content=combined_input),
]

result = model.invoke(messages)

print("\n--- Generated Response ---")
print(result.content)