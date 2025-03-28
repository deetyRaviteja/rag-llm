import os
import pickle
import numpy as np
import faiss
from embeddings import get_embedding
from preprocess_docs import split_text

# Ensure the index directory exists
if not os.path.exists("index"):
    os.makedirs("index")

# Load raw documentation and preprocess it
with open("data/jenkins_docs.txt", "r", encoding="utf-8") as f:
    text = f.read()

chunks = split_text(text)

# Generate embeddings for each chunk
embeddings_list = [get_embedding(chunk) for chunk in chunks]
embeddings_array = np.vstack(embeddings_list)

# Build a FAISS index (using L2 distance)
dimension = embeddings_array.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings_array)

# Save the FAISS index and document chunks for later retrieval
with open("index/faiss_index.pkl", "wb") as f:
    pickle.dump(index, f)
with open("index/doc_chunks.pkl", "wb") as f:
    pickle.dump(chunks, f)

print("FAISS index built and saved!")
