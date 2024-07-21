import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Load dataset
data = pd.read_csv('gift_card_transactions.csv')

# Encode categorical features
label_encoders = {}
for column in ['merchant_id', 'location', 'gift_card_type']:
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column])
    label_encoders[column] = le

# Features and target
X = data[['amount', 'user_id', 'merchant_id', 'location', 'gift_card_type']]
y = data['is_fraud']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model and label encoders
joblib.dump(model, 'gift_card_fraud_detection_model.pkl')
joblib.dump(label_encoders, 'gift_card_label_encoders.pkl')

print("Gift card fraud detection model trained and saved.")
