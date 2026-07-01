import json
import pickle
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from config import EMBEDDING_MODEL

model = SentenceTransformer(EMBEDDING_MODEL)

with open("data/catalog.json", "r", encoding="utf-8") as f:
    catalog = json.load(f)

documents = []

for item in catalog:

    text = f"""
Assessment Name: {item.get('name', '')}

Description:
{item.get('description', '')}

Categories:
{', '.join(item.get('keys', []))}

Job Levels:
{', '.join(item.get('job_levels', []))}

Languages:
{', '.join(item.get('languages', []))}

Duration:
{item.get('duration', '')}

Remote:
{item.get('remote', '')}

Adaptive:
{item.get('adaptive', '')}
"""

    documents.append(text)

print("Creating embeddings...")

embeddings = model.encode(
    documents,
    show_progress_bar=True
)

embeddings = np.array(embeddings).astype("float32")

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

faiss.write_index(index, "vectorstore/index.faiss")

with open("vectorstore/metadata.pkl", "wb") as f:
    pickle.dump(catalog, f)

print("=================================")
print("Vector Database Created Successfully")
print(f"Total Assessments : {len(catalog)}")
print("=================================")