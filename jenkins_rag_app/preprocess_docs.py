# preprocess_docs.py
import pickle

def split_text(text, chunk_size=500):
    words = text.split()
    chunks = [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]
    return chunks

if __name__ == "__main__":
    with open("data/jenkins_docs.txt", "r", encoding="utf-8") as f:
        text = f.read()
    chunks = split_text(text)
    with open("data/doc_chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)
    print(f"Documentation split into {len(chunks)} chunks and saved!")
