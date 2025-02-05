from flask import Flask, request, jsonify
from flask_cors import CORS  # Add this line
import joblib

# Initialize the Flask app
app = Flask(__name__)

# Load the trained model
model = joblib.load('trained_model.pkl')

# Define a route for the home page


@app.route("/")
def home():
    return "<h1>Welcome to the Phishing Link Scanner</h1><p>Use the /scan route to check URLs.</p>"

# Define a route for scanning URLs


@app.route("/scan", methods=["GET"])
def scan():
    # Get the URL parameter from the request
    url = request.args.get("url")

    if not url:
        return jsonify({"error": "No URL provided."}), 400

    # Preprocess the URL (example feature extraction logic)
    features = extract_features(url)

    # Predict using the loaded model
    prediction = model.predict([features])[0]

    # Return the result as JSON
    if prediction == 1:
        return jsonify({"message": "Phishing detected!"}), 200
    else:
        return jsonify({"message": "Safe link."}), 200

# Feature extraction function (example logic)


def extract_features(url):
    return [len(url), len(url.split('/')[2]), url.count('.')]


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
