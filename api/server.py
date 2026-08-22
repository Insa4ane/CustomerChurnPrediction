import joblib
from fastapi import FastAPI
import pandas as pd
app=FastAPI()
PIPELINE_MODEL = joblib.load("model/model.joblib")

@app.get("/")
def powitanie():
    return {"status": "sukces", "wiadomosc": "API dziala w nowym folderze!"}

@app.post("/columns")
def kolumny():
    return {"status": "sukces"}

@app.post("/predict")
def predict_churn(data: dict):
    df_input = pd.DataFrame([data])
    result = PIPELINE_MODEL.predict(df_input)
    return {
        "status": "sukces",
        "result": int(result[0])
    }







