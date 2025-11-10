from fastapi.testclient import TestClient
from app.api import app

client = TestClient(app)

def test_predict_endpoint_valid_input():
    payload = {
        "gender": "Female",
        "SeniorCitizen": "1",
        "Partner": "No",
        "Dependents": "No",
        "tenure": 16,
        "PhoneService": "Yes",
        "MultipleLines": "Yes",
        "InternetService": "Fiber optic",
        "OnlineSecurity": "No",
        "OnlineBackup": "No",
        "DeviceProtection": "No",
        "TechSupport": "No",
        "StreamingTV": "Yes",
        "StreamingMovies": "Yes",
        "Contract": "Month-to-month",
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check (automatic)",
        "MonthlyCharges": 70.35,
        "TotalCharges": 1135.40
    }

    response = client.post("/predict", json=payload)
    assert response.status_code == 200, "La API no respondió con código 200"

    data = response.json()

    # Validar que estén las claves esperadas
    assert "churn_probability" in data, "Falta 'churn_probability' en la respuesta"
    assert "prediction" in data, "Falta 'prediction' en la respuesta"

    # Validar tipos y rango de valores
    assert isinstance(data["churn_probability"], float), "churn_probability no es float"
    assert 0.0 <= data["churn_probability"] <= 1.0, "churn_probability fuera de rango [0,1]"
    
    # Verificar que la predicción sea 0 o 1
    assert data["prediction"] in [0, 1], "prediction no es 0 o 1"
