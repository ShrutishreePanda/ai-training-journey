from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, precision_score, recall_score

app = FastAPI(title="Model Evaluation API")

class EvaluationInput(BaseModel):
    y_true: list
    y_pred: list
    task_type: str  # "regression" or "classification"

@app.post("/evaluate")
def evaluate_model(data: EvaluationInput):
    y_true = np.array(data.y_true)
    y_pred = np.array(data.y_pred)

    if data.task_type == "regression":
        mse = mean_squared_error(y_true, y_pred)
        r2 = r2_score(y_true, y_pred)

        return {
            "task": "regression",
            "MSE": mse,
            "R2 Score": r2
        }

    elif data.task_type == "classification":
        acc = accuracy_score(y_true, y_pred)
        precision = precision_score(y_true, y_pred)
        recall = recall_score(y_true, y_pred)

        return {
            "task": "classification",
            "Accuracy": acc,
            "Precision": precision,
            "Recall": recall
        }

    return {"error": "Invalid task type"}