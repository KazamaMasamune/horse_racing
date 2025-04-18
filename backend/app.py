
from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd

app = Flask(__name__)
CORS(app, resources={r"/predict": {"origins": "http://localhost:3000"}})  # Explicitly allow localhost:3000

# Load the model and features
model = joblib.load('horse_race_predictor_model.pkl')
features = joblib.load('features.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    new_race = pd.DataFrame([data], columns=features).fillna(0)
    prediction = model.predict(new_race)[0]
    return jsonify({'prediction': 'Winner' if prediction == 1 else 'Not a Winner'})

if __name__ == '__main__':
    app.run(debug=False, port=5050)  # Debug disabled, port 5050
EOF