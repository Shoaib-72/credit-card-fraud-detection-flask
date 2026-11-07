from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd
import os

# Initialize Flask application
app = Flask(__name__)

# Define paths to model and preprocessor
MODEL_PATH = os.path.join('model', 'fraud_model.pkl')
SCALER_PATH = os.path.join('model', 'preprocessor.pkl')
FEATURE_PATH = os.path.join('model', 'feature_names.pkl')

# Load model, scaler, and feature names upon startup
print("Loading model and preprocessor files...")
model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)
feature_names = joblib.load(FEATURE_PATH)
print("Model and preprocessor loaded successfully!")

@app.route('/')
def home():
    """Render the homepage with the input form."""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Extract form data, preprocess it, generate prediction, and render result."""
    try:
        # 1. Extract form values in exact feature order
        input_data = [
            float(request.form['distance_from_home']),
            float(request.form['distance_from_last_transaction']),
            float(request.form['ratio_to_median_purchase_price']),
            float(request.form['repeat_retailer']),
            float(request.form['used_chip']),
            float(request.form['used_pin_number']),
            float(request.form['online_order'])
        ]

        # 2. Convert to DataFrame to match training column structure
        features_df = pd.DataFrame([input_data], columns=feature_names)

        # 3. Apply the pre-fitted StandardScaler
        scaled_features = scaler.transform(features_df)

        # 4. Predict using the trained model
        prediction = int(model.predict(scaled_features)[0])
        
        # 5. Get probability if available
        probability = None
        if hasattr(model, "predict_proba"):
            probabilities = model.predict_proba(scaled_features)[0]
            probability = float(probabilities[1]) # Probability of class 1 (fraud)

        # 6. Render result page
        return render_template('result.html', prediction=prediction, probability=probability)

    except Exception as e:
        return render_template('result.html', prediction=0, probability=None, error=str(e))

if __name__ == '__main__':
    app.run(debug=True, port=5000)