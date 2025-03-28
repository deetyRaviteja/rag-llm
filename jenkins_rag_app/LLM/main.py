# main.py
import streamlit as st
import pickle
import numpy as np
import openai
from embeddings import get_embedding
from rag import query_faiss, generate_answer

# Load the pre-built FAISS index and corresponding document chunks
with open("index/faiss_index.pkl", "rb") as f:
    faiss_index = pickle.load(f)
with open("index/doc_chunks.pkl", "rb") as f:
    doc_chunks = pickle.load(f)

st.set_page_config(page_title="Jenkins RAG App", layout="wide")
st.title("Jenkins Documentation Retrieval & QA")

# Innovative: Add an autocomplete suggestion box (basic example)
query = st.text_input("Enter your Jenkins question:", placeholder="E.g., How do I configure a Jenkins pipeline?")

if query:
    # Generate query embedding
    query_emb = get_embedding(query)
    
    # Retrieve the top 5 most relevant documentation chunks using FAISS
    indices, distances = query_faiss(faiss_index, query_emb, k=5)
    retrieved_chunks = [doc_chunks[i] for i in indices]
    
    # Generate answer using the retrieved chunks as context
    answer = generate_answer(query, retrieved_chunks)
    
    st.subheader("Answer")
    st.write(answer)
    
    # Display source documentation chunks with a simple collapsible section
    st.subheader("Source Documentation Chunks")
    for i, chunk in enumerate(retrieved_chunks):
        with st.expander(f"Source Chunk {i+1} (Distance: {distances[i]:.2f})"):
            st.write(chunk)
    
    # (Optional) Allow users to rate the answer or bookmark for future reference.
    feedback = st.radio("Was this answer helpful?", ("Yes", "No"))
    if feedback:
        st.write("Thanks for your feedback!")
