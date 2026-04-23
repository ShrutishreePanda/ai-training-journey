from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.feature_extraction.text import TfidfVectorizer

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/keywords")
def extract_keywords(data: TextInput):
    vectorizer = TfidfVectorizer(stop_words="english")
    X = vectorizer.fit_transform([data.text])

    scores = zip(vectorizer.get_feature_names_out(), X.toarray()[0])
    sorted_words = sorted(scores, key=lambda x: x[1], reverse=True)

    return {"keywords": [word for word, score in sorted_words[:5]]}