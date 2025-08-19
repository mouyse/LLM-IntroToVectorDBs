import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import Pinecone
from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter

load_dotenv()

if __name__ == '__main__':
    print("Ingesting...")
    loader = TextLoader("wikipedia.txt", encoding="utf-8")
    document = loader.load()

    print("Splitting....")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100,  # gives context overlap
        separators=["\n\n", "\n", " ", ""]
    )
    texts = text_splitter.split_documents(document)
    print(f"created {len(texts)} chunks")

    embeddings = OpenAIEmbeddings(openai_api_type=os.environ["OPENAI_API_KEY"])
    print("Ingesting...")

    Pinecone.from_documents(texts, embeddings, index_name=os.environ["INDEX_NAME"])