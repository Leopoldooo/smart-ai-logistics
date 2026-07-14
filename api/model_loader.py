import joblib

model = joblib.load("ml_model/model.pkl")


def predict_driver(speed, harsh_braking, fatigue_level):

    prediction = model.predict(
        [[speed, harsh_braking, fatigue_level]]
    )[0]

    if prediction == 1:
        return "Risky Driver"

    return "Safe Driver"