import os
from sys import meta_path
import faiss
import numpy as np
from typing import List, Any
import pickle

from ollama import embeddings
from src.embedding import EmbeddingGenerator
from sentence_transformers import SentenceTransformer

class FaissVectorStore:
    def __init__(self, persist_dir: str = "faiss_store", embedding_model: str = "all-MiniLM-L6-v2", chunk_size: int = 500, chunk_overlap: int = 50):
        self.persist_dir = persist_dir
        os.makedirs(self.persist_dir, exist_ok=True)
        self.index = None
        self.metadata = []
        self.embedding_model_name = embedding_model
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        print(f"[INFO] Loaded embedding model: {embedding_model}")

    def build_from_documents(self, documents: List[Any]):
        print(f"[INFO] Building Faiss index from {len(documents)} raw documents...")
        embedding_gen = EmbeddingGenerator(model_name=self.embedding_model_name,
                                           chunk_size=self.chunk_size,
                                           chunk_overlap=self.chunk_overlap
                                           )
        chunks = embedding_gen.chunk_documents(documents)
        print(f"[INFO] Generated {len(chunks)} chunks from documents")
        embeddings = embedding_gen.embed_chunks(chunks)
        print(f"[INFO] Generated embeddings with shape: {embeddings.shape}")
        metadatas = [{"text": chunk.page_content} for chunk in chunks]
        self.add_embeddings(np.array(embeddings).astype("float32"), metadatas)
        self.save()
        print(f"[INFO] Vector Store built and saved to {self.persist_dir}")
    
    def add_embeddings(self, embeddings: np.ndarray, metadatas: List[dict]):
        dimension = embeddings.shape[1]
        if self.index is None:
            self.index = faiss.IndexFlatL2(dimension)
        
        self.index.add(embeddings)
        if metadatas:
            self.metadata.extend(metadatas)
        print(f"[INFO] Added {embeddings.shape[0]} embeddings to the index. Total embeddings: {self.index.ntotal}")

    def save(self):
        faiss_path = os.path.join(self.persist_dir, "faiss.index")
        meta_path = os.path.join(self.persist_dir, "metadata.pkl")
        faiss.write_index(self.index, faiss_path)
        with open(meta_path, "wb") as f:
            pickle.dump(self.metadata, f)
        print(f"[INFO] Faiss index and metadata saved to {self.persist_dir}")

    def load(self):
        faiss_path = os.path.join(self.persist_dir, "faiss.index")
        meta_path = os.path.join(self.persist_dir, "metadata.pkl")
        self.index = faiss.read_index(faiss_path)
        with open(meta_path, "rb") as f:
            self.metadata = pickle.load(f)
        print(f"[INFO] Loaded Faiss index and metadata from {self.persist_dir}")

    def search(self, query_embedding: np.ndarray, top_k: int = 5):
        D, I = self.index.search(query_embedding, top_k)
        results = []
        for idx, distance in zip(I[0], D[0]):
            meta = self.metadata[idx] if idx < len(self.metadata) else {}
            results.append({"index": idx, "metadata": meta, "distance": distance})
        return results

    def query(self, query_text: str, top_k: int = 5):
        print(f"[INFO] Querying with text: {query_text}")
        query_embedding = self.embedding_model.encode([query_text], show_progress_bar=False).astype("float32")
        return self.search(query_embedding, top_k)