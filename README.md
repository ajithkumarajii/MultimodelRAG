# 📚 Multi-Modal Retrieval-Augmented Generation (RAG) System

This project implements a **Multi-Modal Retrieval-Augmented Generation (RAG)** system that processes both text and images extracted from PDFs to answer user queries. The system uses state-of-the-art models for text and image embeddings, and it employs the Groq platform for generating responses.

## ✨ Features

- **📄 PDF Parsing:** Extracts text and images from PDF files using PyMuPDF.
- **📝 Text Embedding:** Uses the `all-MiniLM-L6-v2` model from the SentenceTransformers library to generate embeddings for text chunks.
- **🖼️ Image Embedding:** Utilizes the `clip-ViT-B-32` model from the SentenceTransformers library for generating embeddings of images.
- **⚡ Faiss Indexing:** Creates separate Faiss indices for text and image embeddings for efficient similarity search.
- **🔍 Multi-Modal Query Processing:** Processes user queries by searching for relevant text and images, then generates a response using the Groq API.
- **🗣️ Response Generation:** The Groq platform is used to generate context-aware responses, referencing both text and images.
- **📊 Results Display:** Displays the generated response, relevant text excerpts, and images related to the query.

## 🛠️ Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/multi-modal-rag.git
   cd multi-modal-rag
   ```
2. **Install the required dependencies:**

  ```bash
  Copy code
  pip install -r requirements.txt
  ```

3. **Set up Groq API:**

Obtain an API key from Groq and replace the placeholder in the code with your API key.
   

## 🚀 Usage

To run the Multi-Modal RAG system:

1. **Specify the PDF path and query:**

   Edit the `pdf_path` and `query` variables in the script with your PDF file path and desired query.

   ```python
   pdf_path = "/path/to/your/pdf/file.pdf"
   query = "Your query here"
   
## 🙏 Acknowledgments

- [Groq](https://groq.com) for providing the API for response generation.
- [SentenceTransformers](https://www.sbert.net) for the pre-trained embedding models.
- [Faiss](https://github.com/facebookresearch/faiss) for the efficient similarity search index.

   
## ✂️ Screenshots

![Screenshot 2024-08-14 122631](https://github.com/user-attachments/assets/654af28a-999b-4913-b29a-65677cf10c12)

![Screenshot 2024-08-14 122642](https://github.com/user-attachments/assets/2bac7f37-eb75-4846-93d6-116d8bfbcdca)

![Screenshot 2024-08-14 122720](https://github.com/user-attachments/assets/97687f34-d741-40a3-92b2-98bbfe9c4656)

![Screenshot 2024-08-14 122654](https://github.com/user-attachments/assets/01c041c3-2579-43d8-b7e5-2f14b9111e5a)
![Screenshot 2024-08-14 122727](https://github.com/user-attachments/assets/3224b57f-68e8-424d-96c4-56cf9dc7dc97)

