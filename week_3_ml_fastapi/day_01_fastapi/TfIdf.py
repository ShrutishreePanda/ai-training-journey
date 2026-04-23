from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

app = FastAPI()

class TextPair(BaseModel):
    text1: str
    text2: str

@app.post("/similarity")
def similarity(data: TextPair):
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform([data.text1, data.text2])

    sim = cosine_similarity(tfidf[0], tfidf[1])[0][0]

    return {"similarity": float(sim)}