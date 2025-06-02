import faiss
import json
import numpy as np
from sentence_transformers import SentenceTransformer
from config import INDEX_PATH, METADATA_PATH, OUTPUT_JSON

embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

class LegalSearch:
    def __init__(self):
        self.index = faiss.read_index(INDEX_PATH)
        with open(METADATA_PATH, 'r') as f:
            self.metadata = json.load(f)
        with open(OUTPUT_JSON, 'r') as f:
            self.documents = json.load(f)

    def search(self, query, k=3):
        query_embed = embedding_model.encode([query])
        distances, indices = self.index.search(np.array(query_embed), k)
        return [self.documents[i] for i in indices[0]]
