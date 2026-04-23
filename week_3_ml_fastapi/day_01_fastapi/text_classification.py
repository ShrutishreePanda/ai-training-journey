from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer

app = FastAPI()

texts = ["I love this", "I hate this", "Amazing product", "Worst ever"]
labels = [1, 0, 1, 0]

model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression())
])

model.fit(texts, labels)

class TextInput(BaseModel):
    text: str

@app.post("/classify")
def classify(data: TextInput):
    pred = model.predict([data.text])
    return {"sentiment": int(pred[0])}