import json
import re
from sentence_transformers import SentenceTransformer, util

# Load model and data
model = SentenceTransformer('all-MiniLM-L6-v2')
with open("data/shl_catalog.json", "r") as f:
    assessments = json.load(f)
assessment_embeddings = model.encode([a["name"] + " " + a["type"] for a in assessments], convert_to_tensor=True)

def recommend_assessments(query, top_k=10, max_duration=None):
    query_embedding = model.encode(query, convert_to_tensor=True)
    scores = util.pytorch_cos_sim(query_embedding, assessment_embeddings)[0]
    scored = list(zip(assessments, scores.tolist()))
    scored.sort(key=lambda x: x[1], reverse=True)

    filtered = []
    for item, score in scored:
        if max_duration and item["duration"] > max_duration:
            continue
        filtered.append(item)
        if len(filtered) == top_k:
            break
    return filtered
