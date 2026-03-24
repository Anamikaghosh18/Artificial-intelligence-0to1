import os 
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings 
from dotenv import load_dotenv
from langchain_chroma import Chroma

load_dotenv()

def load_documents(docs_path="docs"):
       
        if not os.path.exists(docs_path):
            raise FileNotFoundError(f"The directory {docs_path} does not exist. Please create and add your company files.")

        # load all files from docs folder 
        loader = DirectoryLoader(
        path=docs_path, 
        glob="*.txt", 
        loader_cls=TextLoader, 
        loader_kwargs={"encoding": "utf-8"}
    )
        documents = loader.load()

        if len(documents) == 0:
            raise FileNotFoundError(f"No text files found inside the folder {docs_path}, Please add your company documents.")
        for i , doc in enumerate(documents[:2]):
            print(f"\nDocument {i+1}:")
            print(f" Source: {doc.metadata['source']}")
            print(f" Content length: {len(doc.page_content)} chracters")
            print(f" Content preview: {doc.page_content[:100]}...")
            print(f" Metadata: {doc.metadata}")

        return documents

def split_characters(documents, chunk_size=800, chunk_overlap=0):
    text_splitter = CharacterTextSplitter(
         chunk_size=chunk_size, 
         chunk_overlap=chunk_overlap

    )

    chunks = text_splitter.split_documents(documents)

    if chunks:
        for i , chunk in enumerate(chunks[:5]):
              print(f"\n ---chunk ---- {i+1}")
              print(f"Source: {chunk.metadata['source']}")
              print(f"Length: {len(chunk.page_content)} characters")
              print(f"Content: ")
              print(chunk.page_content)
              print("-" * 50)

        if len(chunks) > 5:
            print(f"\n ... and {len(chunks) - 5} more chunks")
     
    return chunks
def create_vector_store(chunks, persist_directory="db/chroma_db"):
    import os

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    persist_directory = os.path.join(BASE_DIR, persist_directory)

    model_name = "BAAI/bge-small-en-v1.5"

    embeddings = HuggingFaceEmbeddings(
        model_name=model_name,
    )

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=persist_directory,
        collection_name="rag_docs",  
        collection_metadata={"hnsw:space": "cosine"}
    )

    print(f" Vector store saved at: {persist_directory}")
    print(f"Stored docs: {vectorstore._collection.count()}")

    return vectorstore
def main():
    # loading the files 
    documents = load_documents("C:/Desktop/Anamika/ML0to1/RAG/docs")

    chunks = split_characters(documents)

    vector_store = create_vector_store(chunks, persist_directory="db/chroma_db")
    
if __name__ == "__main__":
    main()