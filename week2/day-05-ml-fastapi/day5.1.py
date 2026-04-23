from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.linear_model import LogisticRegression
import numpy as np

app = FastAPI()

model = LogisticRegression()

class TrainData(BaseModel):
    X: list
    y: list

@app.post("/train")
def train(data: TrainData):
    X = np.array(data.X)
    y = np.array(data.y)
    model.fit(X, y)
    return {"message": "Model trained"}

class PredictData(BaseModel):
    features: list

@app.post("/predict")
def predict(data: PredictData):
    pred = model.predict([data.features])
    return {"prediction": int(pred[0])}