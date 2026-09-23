import joblib
from functools import lru_cache
from fastapi import FastAPI, HTTPException
import pandas as pd
from config.config import MODEL
from pydantic import BaseModel

app = FastAPI()


@lru_cache
def get_model():
    return joblib.load(MODEL)


class PredictionResponse(BaseModel):
    status: str
    result: str


@app.get("/health")
def health():
    try:
        get_model()
        return {"status": "ok"}
    except FileNotFoundError:
        raise HTTPException(status_code=503, detail="Model nie jest jeszcze wytrenowany")


@app.post("/predict_churn", response_model=PredictionResponse)
def predict_churn(data: dict):
    df_input = pd.DataFrame([data])
    try:
        model = get_model()
    except FileNotFoundError:
        raise HTTPException(status_code=503, detail="Model nie jest jeszcze dostępny")
    try:
        prediction_array = model.predict(df_input)
        pred_value = prediction_array[0]
        return PredictionResponse(
            status="success",
            result=str(pred_value)
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Błędne dane wejściowe: {e}")