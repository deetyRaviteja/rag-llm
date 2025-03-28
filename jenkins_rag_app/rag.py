# rag.py
from transformers import pipeline, AutoTokenizer
import numpy as np
import faiss

# Load a text generation pipeline; for example, GPT-Neo or GPT-J
generator = pipeline("text-generation", model="EleutherAI/gpt-neo-125M")  # smaller model for speed

# Initialize the tokenizer for your model
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neo-125M")
MAX_PROMPT_LENGTH = 1024  # Set based on your model's max token limit

def query_faiss(index, query_embedding, k=5):
    # Search the FAISS index for k nearest neighbors
    distances, indices = index.search(np.array([query_embedding]), k)
    return indices[0], distances[0]

def generate_answer(query, retrieved_chunks):
    # Combine the retrieved chunks and query into a prompt
    context = "\n".join(retrieved_chunks)
    prompt = f"Jenkins Documentation:\n{context}\n\nQuestion: {query}\nAnswer:"
    
    # Tokenize the prompt and truncate if necessary
    prompt_tokens = tokenizer(prompt, truncation=True, max_length=MAX_PROMPT_LENGTH, return_tensors="pt")["input_ids"]
    truncated_prompt = tokenizer.decode(prompt_tokens[0], skip_special_tokens=True)
    
    # Generate answer using the truncated prompt, and generate new tokens
    generated = generator(truncated_prompt, max_new_tokens=50, temperature=0.5)
    answer = generated[0]['generated_text'].strip()
    return answer
