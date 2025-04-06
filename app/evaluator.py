from app.recommender import recommend_assessments

def recall_at_k(predicted, relevant, k):
    predicted_k = predicted[:k]
    hits = len(set(predicted_k).intersection(set(relevant)))
    return hits / len(relevant)

def average_precision_at_k(predicted, relevant, k):
    predicted_k = predicted[:k]
    score = 0.0
    hits = 0
    for i, p in enumerate(predicted_k):
        if p in relevant:
            hits += 1
            score += hits / (i + 1)
    return score / min(len(relevant), k)

def evaluate_all(queries, k=3):
    recalls, maps = [], []
    for q in queries:
        preds = [r['name'] for r in recommend_assessments(q['query'], top_k=k)]
        rec = recall_at_k(preds, q['relevant'], k)
        ap = average_precision_at_k(preds, q['relevant'], k)
        recalls.append(rec)
        maps.append(ap)
    return {
        "MeanRecall@K": sum(recalls) / len(recalls),
        "MAP@K": sum(maps) / len(maps)
    }


