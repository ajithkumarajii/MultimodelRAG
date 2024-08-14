import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from PIL import Image

text_model = SentenceTransformer('all-MiniLM-L6-v2')
image_model = SentenceTransformer('clip-ViT-B-32')

text_index = faiss.IndexFlatL2(384)
image_index = faiss.IndexFlatL2(512)

text_id_to_content = {}
image_id_to_content = {}

def chunk_text(text, chunk_size=1000, overlap=200):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = ' '.join(words[i:i + chunk_size])
        chunks.append(chunk)
    return chunks

def process_text(text_content):
    chunks = chunk_text(text_content)
    embeddings = text_model.encode(chunks)
    for i, emb in enumerate(embeddings):
        text_index.add(np.array([emb]))
        text_id_to_content[text_index.ntotal - 1] = {"content": chunks[i]}

def process_images(image_list):
    for i, img_path in enumerate(image_list):
        with Image.open(img_path) as img:
            emb = image_model.encode(img)
        image_index.add(np.array([emb]))
        image_id_to_content[image_index.ntotal - 1] = {"image_id": i, "image_path": img_path}

def process_query(query, k=2):
    text_query_emb = text_model.encode([query])
    
    D_text, I_text = text_index.search(text_query_emb, k)
    relevant_text = [text_id_to_content.get(idx, {}).get("content", "Not Found") for idx in I_text[0]]
    
    image_query_emb = image_model.encode([query])
    
    D_image, I_image = image_index.search(image_query_emb, k=2)
    relevant_images = [image_id_to_content.get(idx, {}).get("image_path", "Not Found") for idx in I_image[0] if idx != -1]
    
    return relevant_text, relevant_images
