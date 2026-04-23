from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.metrics import classification_report

app = FastAPI()

class InputData(BaseModel):
    y_true: list
    y_pred: list

@app.post("/report")
def report(data: InputData):
    report = classification_report(data.y_true, data.y_pred, output_dict=True)
    return report