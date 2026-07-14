from fastapi import FastAPI
from pydantic import BaseModel

from api.database import SessionLocal, DriverLog
from api.model_loader import predict_driver

app = FastAPI(title="Smart AI Logistics API")


class DriverData(BaseModel):
    speed: float
    harsh_braking: int
    fatigue_level: int


@app.get("/")
def home():
    return {
        "message": "Smart AI Logistics API is running"
    }


@app.post("/predict_driver_behavior")
def predict(data: DriverData):

    prediction = predict_driver(
        data.speed,
        data.harsh_braking,
        data.fatigue_level
    )

    return {
        "prediction": prediction
    }


@app.post("/analyze_risk_score")
def risk(data: DriverData):

    score = (
        data.speed * 0.4 +
        data.harsh_braking * 15 +
        data.fatigue_level * 20
    )

    return {
        "risk_score": round(score, 2)
    }


@app.post("/log_data")
def log_data(data: DriverData):

    prediction = predict_driver(
        data.speed,
        data.harsh_braking,
        data.fatigue_level
    )

    score = (
        data.speed * 0.4 +
        data.harsh_braking * 15 +
        data.fatigue_level * 20
    )

    db = SessionLocal()

    log = DriverLog(
        speed=data.speed,
        harsh_braking=data.harsh_braking,
        fatigue_level=data.fatigue_level,
        prediction=prediction,
        risk_score=round(score, 2)
    )

    db.add(log)
    db.commit()
    db.close()

    return {
        "message": "Data logged successfully",
        "prediction": prediction,
        "risk_score": round(score, 2)
    }