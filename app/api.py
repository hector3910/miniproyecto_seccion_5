from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

model = joblib.load("telco_churn_model.joblib")

app = FastAPI()


class Input(BaseModel):
    gender: str = None
    SeniorCitizen: str = None
    Partner: str = None
    Dependents: str = None
    tenure: float = None
    PhoneService: str = None
    MultipleLines: str = None
    InternetService: str = None
    OnlineSecurity: str = None
    OnlineBackup: str = None
    DeviceProtection: str = None
    TechSupport: str = None
    StreamingTV: str = None
    StreamingMovies: str = None
    Contract: str = None
    PaperlessBilling: str = None
    PaymentMethod: str = None
    MonthlyCharges: float = None
    TotalCharges: float = None


@app.post("/predict")
def predict(data: Input):
    X = pd.DataFrame([data.dict()])
    proba = model.predict_proba(X)[0][1]
    return {
        "churn_probability": round(float(proba), 2),
        "prediction": "Yes" if proba > 0.5 else "No"
    }
