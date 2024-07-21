import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Load dataset
data = pd.read_csv('credit_card_transactions.csv')

# Encode categorical features
label_encoders = {}
for column in ['merchant_id', 'location']:
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column])
    label_encoders[column] = le

# Features and target
X = data[['amount', 'user_id', 'merchant_id', 'location']]
y = data['is_fraud']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model and label encoders
joblib.dump(model, 'credit_card_fraud_detection_model.pkl')
joblib.dump(label_encoders, 'label_encoders.pkl')

print("Credit card fraud detection model trained and saved.")
