# embeddings.py
from sentence_transformers import SentenceTransformer
import numpy as np

# Load the model (this may take a moment the first time)
model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embedding(text):
    # Encode the text into a vector (numpy array)
    embedding = model.encode(text, convert_to_numpy=True)
    return embedding

