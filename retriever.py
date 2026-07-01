import pickle
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from config import EMBEDDING_MODEL, TOP_K

# Lazy-loaded model
_model = None

def get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer(EMBEDDING_MODEL)
    return _model

# Load FAISS index once
index = faiss.read_index("vectorstore/index.faiss")

with open("vectorstore/metadata.pkl", "rb") as f:
    metadata = pickle.load(f)


def retrieve(query, k=TOP_K):
    model = get_model()

    embedding = model.encode([query])
    embedding = np.array(embedding).astype("float32")

    distances, indices = index.search(embedding, k)

    results = []

    for idx in indices[0]:
        if idx == -1:
            continue

        item = metadata[idx]

        results.append({
            "entity_id": item.get("entity_id"),
            "name": item.get("name", ""),
            "link": item.get("link", ""),
            "description": item.get("description", ""),
            "job_levels": item.get("job_levels", []),
            "languages": item.get("languages", []),
            "duration": item.get("duration", ""),
            "keys": item.get("keys", []),
            "remote": item.get("remote", ""),
            "adaptive": item.get("adaptive", "")
        })

    return results