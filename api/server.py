import joblib
from fastapi import FastAPI, HTTPException
import pandas as pd
from config.config import MODEL
from pydantic import BaseModel

app = FastAPI()
PIPELINE_MODEL = joblib.load(MODEL)


class PredictionResponse(BaseModel):
    status: str
    result: str

@app.post("/predict", response_model=PredictionResponse)
def predict_churn(data: dict):
    df_input = pd.DataFrame([data])
    try:
        prediction_array = PIPELINE_MODEL.predict(df_input)
        pred_value = prediction_array[0]
        return PredictionResponse(
            status="success",
            result=str(pred_value)
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Błędne dane wejściowe: {e}")