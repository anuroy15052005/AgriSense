import os

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

DATA_PATH = os.path.join("data", "Crop_recommendation.csv")
MODEL_PATH = os.path.join("models", "crop_model.joblib")


def train_and_save_model() -> float:
    df = pd.read_csv(DATA_PATH)
    X = df.drop(columns=["label"])
    y = df["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model = RandomForestClassifier(
        n_estimators=200,
        random_state=42,
        class_weight="balanced",
    )
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    accuracy = accuracy_score(y_test, preds)

    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    return accuracy


if __name__ == "__main__":
    accuracy = train_and_save_model()
    print(f"Model trained and saved to {MODEL_PATH}")
    print(f"Test accuracy: {accuracy:.4f}")
