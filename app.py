import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np

class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

app = FastAPI(title="Nubank Fraud Detection API")

try:
    model = joblib.load('model.pkl')
    CLASSES = ['setosa', 'versicolor', 'virginica']
except Exception as e:
    print(f"Error al cargando el modelo: {e}")


@app.get("/")
def home():
    return {
        "API": "Nubank Fraud Detection Service",
        "Version": "1.0.0",
        "Algorithm": "RandomForest",
        "Usage": "POST to /predict with Iris features"
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/predict")
def predict(data: IrisInput):
    try:
        features = np.array([[
            data.sepal_length,
            data.sepal_width,
            data.petal_length,
            data.petal_width
        ]])

        prediction_index = int(model.predict(features)[0])
        probabilities = model.predict_proba(features)[0]

        return {
            "prediction": CLASSES[prediction_index],
            "prediction_index": prediction_index,
            "probabilities": {
                CLASSES[0]: round(probabilities[0], 2),
                CLASSES[1]: round(probabilities[1], 2),
                CLASSES[2]: round(probabilities[2], 2)
            },
            "confidence": round(float(np.max(probabilities)), 2),
            "status": "success"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))