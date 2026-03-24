from langchain_chroma import Chroma 
from langchain_community.embeddings import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

persistent_directory = r"C:\Desktop\Anamika\ML0to1\RAG\db\chroma_db"

model_name = "BAAI/bge-small-en-v1.5"

embeddings = HuggingFaceEmbeddings(
    model_name=model_name,
)

import os
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
persist_directory = os.path.join(BASE_DIR, "db", "chroma_db")

embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)

db = Chroma(
    persist_directory=persist_directory,
    embedding_function=embeddings,
    collection_name="rag_docs"  )

query = "Which island does SpaceX lease for its launches in the Pacific?"

retriever = db.as_retriever(search_kwargs={"k": 3})

relevant_docs = retriever.invoke(query)

print(f"User Query: {query}")
if not relevant_docs:
    print("❌ No documents retrieved")
else:
    for i, doc in enumerate(relevant_docs, 1):
        print(f"\nDocument {i}:")
        print(doc.page_content[:300])