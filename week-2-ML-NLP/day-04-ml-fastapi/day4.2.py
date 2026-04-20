from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

app = FastAPI()

class RegressionInput(BaseModel):
    y_true: list
    y_pred: list

@app.post("/regression-metrics")
def regression_metrics(data: RegressionInput):
    mae = mean_absolute_error(data.y_true, data.y_pred)
    rmse = np.sqrt(mean_squared_error(data.y_true, data.y_pred))

    return {
        "MAE": mae,
        "RMSE": rmse
    }