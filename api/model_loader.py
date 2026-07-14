def predict_driver(speed, harsh_braking, fatigue_level):

    if speed > 80 or harsh_braking >= 3 or fatigue_level >= 4:
        return "Risky Driver"

    return "Safe Driver"