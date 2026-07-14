import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

import joblib

# Load dataset
data = pd.read_csv("ml_model/dataset.csv")

# Features
X = data[["speed", "harsh_braking", "fatigue_level"]]

# Target
y = data["risky"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = LogisticRegression()

model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Evaluate
accuracy = accuracy_score(y_test, predictions)

print("\nModel Accuracy:", accuracy)

print("\nConfusion Matrix:")

print(confusion_matrix(y_test, predictions))

# Save model
joblib.dump(model, "ml_model/model.pkl")

print("\nModel saved successfully!")