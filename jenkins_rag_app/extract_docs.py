# extract_docs.py
import requests
from bs4 import BeautifulSoup

def extract_jenkins_docs(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Customize the extraction based on Jenkins documentation layout
    docs = soup.get_text(separator="\n")
    return docs

if __name__ == "__main__":
    url = "https://www.jenkins.io/doc/"
    docs = extract_jenkins_docs(url)
    with open("data/jenkins_docs.txt", "w", encoding="utf-8") as f:
        f.write(docs)
    print("Jenkins documentation extracted and saved!")
