from fastapi import FastAPI, Query
from pydantic import BaseModel
from app.recommender import recommend_assessments

app = FastAPI()

class QueryInput(BaseModel):
    query: str
    max_duration: int | None = None

@app.post("/recommend")
def get_recommendations(input: QueryInput):
    results = recommend_assessments(input.query, max_duration=input.max_duration)
    return results
