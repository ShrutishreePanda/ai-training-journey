from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.metrics import confusion_matrix, f1_score

app = FastAPI()

class InputData(BaseModel):
    y_true: list
    y_pred: list

@app.post("/classification-metrics")
def classification_metrics(data: InputData):
    cm = confusion_matrix(data.y_true, data.y_pred).tolist()
    f1 = f1_score(data.y_true, data.y_pred, average="weighted")

    return {
        "confusion_matrix": cm,
        "f1_score": f1
    }