import requests
import numpy as np
from sentence_transformers import SentenceTransformer

# Initialize Embedding Model
model = SentenceTransformer('all-MiniLM-L6-v2')
ENDEE_URL = "http://localhost:8080" # Default Endee port

class EndeeManager:
    def __init__(self, index_name="products"):
        self.index_name = index_name

    def create_index(self, dimension=384):
        # Create an index in Endee
        payload = {"name": self.index_name, "dimension": dimension, "metric": "cosine"}
        return requests.post(f"{ENDEE_URL}/create_index", json=payload)

    def upsert_data(self, items):
        """
        items: List of dicts with {'id': str, 'text': str, 'metadata': dict}
        """
        for item in items:
            vector = model.encode(item['text']).tolist()
            payload = {
                "id": item['id'],
                "vector": vector,
                "metadata": item['metadata']
            }
            requests.post(f"{ENDEE_URL}/indices/{self.index_name}/upsert", json=payload)

    def search(self, query, top_k=3):
        query_vector = model.encode(query).tolist()
        payload = {"vector": query_vector, "top_k": top_k}
        response = requests.post(f"{ENDEE_URL}/indices/{self.index_name}/search", json=payload)
        return response.json()
