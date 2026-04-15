import re
import nltk
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords

# Download stopwords (runs once)
nltk.download('stopwords', quiet=True)

app = FastAPI(title="Week 2 Day 1 - NLP API")

# Stopwords
STOPWORDS = set(stopwords.words('english'))

# Sample corpus to train TF-IDF
corpus = [
    "machine learning is amazing",
    "fastapi is a modern web framework",
    "natural language processing is powerful",
    "python is widely used in data science"
]

# Initialize and fit vectorizer
vectorizer = TfidfVectorizer()
vectorizer.fit(corpus)

# Request Models
class TextInput(BaseModel):
    text: str

class TextListInput(BaseModel):
    texts: list[str]

# Preprocessing function
def preprocess_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)  # remove punctuation
    words = text.split()
    words = [w for w in words if w not in STOPWORDS]
    return " ".join(words)

# Root endpoint
@app.get("/")
def home():
    return {"message": "NLP FastAPI running", "endpoints": ["/clean", "/vectorize"]}

# Clean text endpoint
@app.post("/clean")
def clean_text(payload: TextInput):
    if not payload.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")

    cleaned = preprocess_text(payload.text)

    return {
        "original": payload.text,
        "cleaned": cleaned
    }

# Vectorize endpoint
@app.post("/vectorize")
def vectorize_text(payload: TextListInput):
    if not payload.texts:
        raise HTTPException(status_code=400, detail="Texts list cannot be empty")

    # Preprocess each text
    cleaned_texts = [preprocess_text(t) for t in payload.texts]

    # Convert to TF-IDF vectors
    vectors = vectorizer.transform(cleaned_texts).toarray()

    return {
        "cleaned_texts": cleaned_texts,
        "vector_shape": vectors.shape,
        "vectors_sample": vectors.tolist()
    }