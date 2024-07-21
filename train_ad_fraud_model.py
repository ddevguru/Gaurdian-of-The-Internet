import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

# Load dataset
data = pd.read_csv('ad_data.csv')

# Drop non-numeric feature
data = data.drop(columns=['ip_address'])

# Encode categorical features
label_encoders = {}
for column in ['ad_platform', 'country', 'browser']:
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column])
    label_encoders[column] = le

# Features and target
X = data[['ad_platform', 'clicks', 'impressions', 'country', 'browser']]
y = data['is_fraud']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model and label encoders
joblib.dump(model, 'ad_fraud_detection_model.pkl')
joblib.dump(label_encoders, 'ad_label_encoders.pkl')

print("Ad fraud detection model trained and saved.")
