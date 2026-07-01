import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
from config import EMBEDDING_MODEL, TOP_K

# Load embedding model
model = SentenceTransformer(EMBEDDING_MODEL)

# Load FAISS index
index = faiss.read_index("vectorstore/index.faiss")

# Load metadata
with open("vectorstore/metadata.pkl", "rb") as f:
    metadata = pickle.load(f)


def retrieve(query, k=TOP_K):
    """
    Retrieve top-k most relevant SHL assessments
    """

    embedding = model.encode([query])

    embedding = np.array(embedding).astype("float32")

    distances, indices = index.search(embedding, k)

    results = []

    seen = set()

    for idx in indices[0]:

        if idx == -1:
            continue

        item = metadata[idx]

        # Remove duplicate assessments
        if item.get("entity_id") in seen:
            continue

        seen.add(item.get("entity_id"))

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