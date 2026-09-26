import os
from pathlib import Path

from flask import Flask, jsonify, request, send_from_directory

from backend.prediction import predict_crop
from backend.schemas import validate_input

BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"

app = Flask(__name__, static_folder=None)


@app.route("/")
def home():
    return send_from_directory(FRONTEND_DIR, "index.html")


@app.route("/<path:filename>")
def frontend_file(filename):
    return send_from_directory(FRONTEND_DIR, filename)


@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json(silent=True)

    if not isinstance(data, dict) or not data:
        return jsonify({
            "error": "No input data provided"
        }), 400

    valid, error = validate_input(data)

    if not valid:
        return jsonify({
            "error": error
        }), 400

    try:
        crop = predict_crop(
            float(data["N"]),
            float(data["P"]),
            float(data["K"]),
            float(data["temperature"]),
            float(data["humidity"]),
            float(data["ph"]),
            float(data["rainfall"])
        )

        return jsonify({
            "crop": crop
        })

    except Exception:
        return jsonify({
            "error": "Prediction failed. Please try again."
        }), 500


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", "5000")),
        debug=os.getenv("FLASK_DEBUG", "0") == "1"
    )