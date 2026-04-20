from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np

app = FastAPI()

class ThresholdInput(BaseModel):
    y_true: list
    y_prob: list
    threshold: float

@app.post("/threshold-eval")
def threshold_eval(data: ThresholdInput):
    y_pred = [1 if p >= data.threshold else 0 for p in data.y_prob]

    tp = sum((yt == 1 and yp == 1) for yt, yp in zip(data.y_true, y_pred))
    fp = sum((yt == 0 and yp == 1) for yt, yp in zip(data.y_true, y_pred))
    fn = sum((yt == 1 and yp == 0) for yt, yp in zip(data.y_true, y_pred))

    precision = tp / (tp + fp + 1e-10)
    recall = tp / (tp + fn + 1e-10)

    return {
        "threshold": data.threshold,
        "precision": precision,
        "recall": recall
    }