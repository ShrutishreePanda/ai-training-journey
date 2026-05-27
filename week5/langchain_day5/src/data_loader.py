from pathlib import Path
from typing import List, Any
from langchain_community.document_loaders import PyPDFLoader, TextLoader, CSVLoader
from langchain_community.document_loaders import Docx2txtLoader
from langchain_community.document_loaders import UnstructuredWordDocumentLoader
from langchain_community.document_loaders import JSONLoader

def load_all_documents(data_dir: str) -> List[Any]:
    
    #Load all documents from the specified directory
    data_path= Path(data_dir).resolve()
    print(f"[Debug] Data Path: {data_path}")
    documents = []

    #pdf files
    pdf_files = list(data_path.rglob("**/*.pdf"))
    print(f"[Debug] Found {len(pdf_files)} PDF files: {[str(pdf) for pdf in pdf_files]}")
    for pdf_file in pdf_files:
        print(f"[Debug] Loading PDF file: {pdf_file}")
        try:
            loader = PyPDFLoader(str(pdf_file))
            loaded = loader.load()
            print(f"[Debug] Loaded {len(loaded)} documents from {pdf_file}")
            documents.extend(loaded)
        except Exception as e:
            print(f"[Error] Failed to load PDF file: {pdf_file}. Error: {e}")

    #text files
    text_files = list(data_path.rglob("**/*.txt"))
    print(f"[Debug] Found {len(text_files)} Text files: {[str(txt) for txt in text_files]}")
    for text_file in text_files:
        print(f"[Debug] Loading Text file: {text_file}")
        try:
            loader = TextLoader(str(text_file))
            loaded = loader.load()
            print(f"[Debug] Loaded {len(loaded)} documents from {text_file}")
            documents.extend(loaded)
        except Exception as e:
            print(f"[Error] Failed to load Text file: {text_file}. Error: {e}")
    
    #csv files
    csv_files = list(data_path.rglob("**/*.csv"))
    print(f"[Debug] Found {len(csv_files)} CSV files: {[str(csv) for csv in csv_files]}")
    for csv_file in csv_files:
        print(f"[Debug] Loading CSV file: {csv_file}")
        try:
            loader = CSVLoader(str(csv_file))
            loaded = loader.load()
            print(f"[Debug] Loaded {len(loaded)} documents from {csv_file}")
            documents.extend(loaded)
        except Exception as e:
            print(f"[Error] Failed to load CSV file: {csv_file}. Error: {e}")


    #docx files
    docx_files = list(data_path.rglob("**/*.docx"))
    print(f"[Debug] Found {len(docx_files)} DOCX files: {[str(docx) for docx in docx_files]}")
    for docx_file in docx_files:
        print(f"[Debug] Loading DOCX file: {docx_file}")
        try:
            loader = UnstructuredWordDocumentLoader(str(docx_file))
            loaded = loader.load()
            print(f"[Debug] Loaded {len(loaded)} documents from {docx_file}")
            documents.extend(loaded)
        except Exception as e:
            print(f"[Error] Failed to load DOCX file: {docx_file}. Error: {e}")
    

    #sql files
    sql_files = list(data_path.rglob("**/*.sql"))
    print(f"[Debug] Found {len(sql_files)} SQL files: {[str(sql) for sql in sql_files]}")
    for sql_file in sql_files:
        print(f"[Debug] Loading SQL file: {sql_file}")
        try:
            loader = TextLoader(str(sql_file))
            loaded = loader.load()
            print(f"[Debug] Loaded {len(loaded)} documents from {sql_file}")
            documents.extend(loaded)
        except Exception as e:
            print(f"[Error] Failed to load SQL file: {sql_file}. Error: {e}")

    #json files
    json_files = list(data_path.rglob("**/*.json"))
    print(f"[Debug] Found {len(json_files)} JSON files: {[str(json) for json in json_files]}")
    for json_file in json_files:
        print(f"[Debug] Loading JSON file: {json_file}")
        try:
            loader = JSONLoader(str(json_file))
            loaded = loader.load()
            print(f"[Debug] Loaded {len(loaded)} documents from {json_file}")
            documents.extend(loaded)
        except Exception as e:
            print(f"[Error] Failed to load JSON file: {json_file}. Error: {e}")


    return documents