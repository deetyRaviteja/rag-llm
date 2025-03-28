# Jenkins RAG Application

This project is a Retrieval-Augmented Generation (RAG) application designed to interact with Jenkins documentation, allowing users to input queries and receive generated answers based on retrieved document chunks.&#8203;:contentReference[oaicite:2]{index=2}

## Features

## Features
- Supports document retrieval
- Uses AI-based embeddings for search


## Prerequisites

Before running this application, ensure you have the following installed:

Before running this project, ensure you have the following installed:

- **Python 3.12** (or a compatible version)  
  It is recommended to use a virtual environment for this project.

- **pip** (Python package installer)

- **Required Python Packages:**  
  All required packages are listed in the `requirements.txt` file. These include:
  - `streamlit` – for building the web UI.
  - `faiss-cpu` – for vector indexing and nearest neighbor search.
  - `sentence-transformers` – for generating text embeddings.
  - `transformers` – for using the text generation pipeline.
  - `beautifulsoup4` – for web scraping Jenkins documentation.
  - `requests` – for handling HTTP requests.
  - `numpy` – for numerical operations.
  - `scikit-learn` – for any additional data processing.

- **Optional:**  
  - Developer Mode (or running Python as an administrator) on Windows may be required to enable symlink support for the Hugging Face hub cache.
  - If using the OpenAI API instead of open-source models, you must have an API key from [OpenAI](https://platform.openai.com/account/api-keys).

Make sure you install these prerequisites by running:

pip install -r requirements.txt


## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/jenkins_rag_app.git
2.**Navigate to the project directory:**


bash
Copy
Edit
cd jenkins_rag_app

3Installation

Clone the repository:

git clone https://github.com/yourusername/jenkins_rag_app.git

Navigate to the project directory:

cd jenkins_rag_app

Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the required packages:

pip install -r requirements.txt

Usage

To run the application, execute the main.py script:

python main.py

Follow the on-screen prompts to enter your Jenkins-related queries and receive generated answers.

Troubleshooting

If you encounter the error:

IndexError: index out of range in self

This may be due to an issue with the input data or the retrieval process. Ensure that your query is well-formed and that the retrieved_chunks variable contains the expected data. For more detailed debugging, consider adding print statements or using a debugger to inspect the state of variables at different points in the code.

Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

License

This project is licensed under the MIT License.

