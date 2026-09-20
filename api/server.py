import joblib
from fastapi import FastAPI, HTTPException
import pandas as pd
from config.config import MODEL
app=FastAPI()
PIPELINE_MODEL = joblib.load(MODEL)

@app.post("/predict")
def predict_churn(data: dict):
    df_input = pd.DataFrame([data])
    try:
        result = PIPELINE_MODEL.predict(df_input)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Błędne dane wejściowe: {e}")
    return {
        "status": "sukces",
        "result": str(result[0])
    }







