import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import pickle

# Load your dataset
df = pd.read_csv('C:/Users/Aninda/Desktop/DESKTOP DOCUMENTS/EDUCATION_ABHRA/PROJECTS/TECHNICAL SEMINAR/traffic_accident_prediction.csv')



# List your categorical columns
categorical_cols = ['Weather', 'Road_Type', 'Time_of_Day', 'Road_Condition', 'Vehicle_Type', 'Road_Light_Condition']

# Encode categorical columns and save encoders
encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    df[col] = df[col].astype(str)
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

# Encode the target column
target_le = LabelEncoder()
df['Accident_Severity'] = target_le.fit_transform(df['Accident_Severity'])
y = df['Accident_Severity']

# Encode the target column
target_le = LabelEncoder()
df['Accident_Severity'] = target_le.fit_transform(df['Accident_Severity'])
y = df['Accident_Severity']


# Save the target encoder
with open('target_encoder.pkl', 'wb') as f:
    pickle.dump(target_le, f)

# Prepare your features
FEATURES = [
    'Weather', 'Road_Type', 'Time_of_Day', 'Traffic_Density', 'Speed_Limit',
    'Number_of_Vehicles', 'Driver_Alcohol', 'Road_Condition',
    'Vehicle_Type', 'Driver_Age', 'Driver_Experience', 'Road_Light_Condition'
]
X = df[FEATURES]

# Train your model
model = RandomForestClassifier()
model.fit(X, y)

# Save the model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

# Save the encoders
with open('encoders.pkl', 'wb') as f:
    pickle.dump(encoders, f)