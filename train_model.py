from pathlib import Path

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "Crop_recommendation.csv"
MODEL_PATH = BASE_DIR / "models" / "crop_recommendation_model.pkl"
FEATURE_COLUMNS = [
	"N", "P", "K", "temperature", "humidity", "ph", "rainfall"
]


def train() -> None:
	data = pd.read_csv(DATA_PATH)
	features = data[FEATURE_COLUMNS]
	labels = data["label"]

	train_features, test_features, train_labels, test_labels = train_test_split(
		features,
		labels,
		test_size=0.2,
		random_state=42,
		stratify=labels
	)

	model = RandomForestClassifier(
		n_estimators=200,
		random_state=42,
		n_jobs=-1
	)
	model.fit(train_features, train_labels)

	accuracy = accuracy_score(test_labels, model.predict(test_features))
	model.fit(features, labels)
	MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
	joblib.dump(model, MODEL_PATH)
	print(f"Validation accuracy: {accuracy:.3f}")
	print(f"Saved model to {MODEL_PATH}")


if __name__ == "__main__":
	train()
