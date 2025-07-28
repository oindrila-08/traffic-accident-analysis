import pickle
import numpy as np
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Load model and encoders
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('encoders.pkl', 'rb') as f:
    encoders = pickle.load(f)
with open('target_encoder.pkl', 'rb') as f:
    target_encoder = pickle.load(f)

# List of features used in the model
FEATURES = [
    'Weather', 'Road_Type', 'Time_of_Day', 'Traffic_Density', 'Speed_Limit',
    'Number_of_Vehicles', 'Driver_Alcohol', 'Road_Condition',
    'Vehicle_Type', 'Driver_Age', 'Driver_Experience', 'Road_Light_Condition'
]

@app.route('/')
def index():
    dropdowns = {
        'Weather': ['Clear', 'Rainy', 'Foggy', 'Stormy', 'Snowy'],
        'Road_Type': ['City Road', 'Rural Road', 'Highway', 'Mountain Road'],
        'Time_of_Day': ['Morning', 'Afternoon', 'Evening', 'Night'],
        'Traffic_Density': ['0.0', '1.0', '2.0'],
        'Road_Condition': ['Dry', 'Wet', 'Icy', 'Under Construction'],
        'Vehicle_Type': ['Car', 'Truck', 'Bus', 'Motorcycle'],
        'Road_Light_Condition': ['Daylight', 'Artificial Light', 'No Light'],
    }
    return render_template('dashboard.html', dropdowns=dropdowns)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    X = []

    for feat in FEATURES:
        val = data.get(feat, "")
        if feat in encoders:
            try:
                val = encoders[feat].transform([val])[0]
            except Exception:
                val = 0
        else:
            try:
                val = float(val)
            except Exception:
                val = 0.0
        X.append(val)

    X = np.array(X).reshape(1, -1)

    # Predict
    pred = model.predict(X)[0]
    proba = model.predict_proba(X).max()

    # Decode label from target encoder
    try:
        pred_label = target_encoder.inverse_transform([pred])[0]
    except Exception as e:
        print("Decoding error:", e)
        pred_label = str(pred)

    # Normalize label to standard 3 categories
    severity_map = {
        'fatal': 'High',
        'major': 'High',
        'severe': 'High',
        'high': 'High',
        'moderate': 'Moderate',
        'medium': 'Moderate',
        'low': 'Low',
        'minor': 'Low',
        'no accident': 'Low',
        'none': 'Low'
    }

    severity_level = severity_map.get(str(pred_label).strip().lower(), 'Low')

    # Decide if accident occurred
    accident_occurrence = "Yes" if severity_level != 'Low' else "No"

    return jsonify({
        'accident': accident_occurrence,
        'severity': severity_level,
        'probability': f"{proba*100:.2f}%"
    })

if __name__ == '__main__':
    app.run(debug=True)