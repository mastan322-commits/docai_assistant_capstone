from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load embedding model once
model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_chunks(chunks: list[str], index_path="vector_index.faiss"):
    """
    Convert chunks into embeddings and store them in FAISS index.
    """
    embeddings = model.encode(chunks)
    dim = embeddings.shape[1]

    # Create FAISS index
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))

    # Save index to disk
    faiss.write_index(index, index_path)
    return index

def search_chunks(query: str, chunks: list[str], index_path="vector_index.faiss", top_k=3):
    """
    Embed query, search FAISS index, return top-k chunks.
    """
    # Load index
    index = faiss.read_index(index_path)

    # Embed query
    query_embedding = model.encode([query])

    # Search
    D, I = index.search(np.array(query_embedding), top_k)
    results = [chunks[i] for i in I[0]]
    return results