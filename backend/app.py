from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
import logging

app = Flask(__name__)
CORS(app)  # Allow all origins for development

# Load the trained model and dataset
model = joblib.load('trained_model.pkl')
dataset = pd.read_csv(
    'C:/Users/DELL/OneDrive/Desktop/Phising Link scanner/model/dataset_phishing.csv')

# Get the feature names used during training
feature_names = model.feature_names_in_  # Requires scikit-learn >= 1.0

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.route("/")
def home():
    return "<h1>Welcome to the Phishing Link Scanner</h1><p>Use the /scan route to check URLs.</p>"


@app.route("/scan", methods=["GET"])
def scan():
    url = request.args.get("url")
    logger.info(f"Received URL for scanning: {url}")

    if not url:
        logger.error("No URL provided.")
        return jsonify({"error": "No URL provided."}), 400

    # Search for the URL in the dataset
    result = dataset[dataset['url'] == url]

    if result.empty:
        logger.error("URL not found in the dataset.")
        return jsonify({"error": "URL not found in the dataset."}), 404

    # Extract features for the found URL
    try:
        # Ensure the features match the ones used during training
        features = result[feature_names]
        logger.info(f"Extracted features: {features.to_dict()}")
    except KeyError as e:
        logger.error(f"Feature mismatch: {e}")
        return jsonify({"error": f"Feature mismatch: {e}"}), 400

    # Predict using the loaded model
    try:
        prediction = model.predict(features)[0]
        # Confidence for phishing class
        confidence = model.predict_proba(features)[0][1]
    except Exception as e:
        logger.error(f"Prediction failed: {e}")
        return jsonify({"error": f"Prediction failed: {e}"}), 500

    # Return the result as JSON
    result = {
        "prediction": prediction,
        "message": "Phishing detected!" if prediction == "phishing" else "Safe link",
        "confidence": confidence if prediction == "phishing" else 1-confidence
    }

    logger.info(f"Prediction result: {result}")
    return jsonify(result), 200


if __name__ == "__main__":
    app.run(debug=True)
