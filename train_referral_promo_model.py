import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Load dataset
data = pd.read_csv('referral_promo_data.csv')

# Encode categorical features
label_encoders = {}
for column in ['referral_code', 'promo_code']:
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column])
    label_encoders[column] = le

# Features and target
X = data[['referral_code', 'promo_code', 'num_referrals', 'total_spent']]
y = data['is_fraud']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model and label encoders
joblib.dump(model, 'referral_promo_fraud_detection_model.pkl')
joblib.dump(label_encoders, 'referral_promo_label_encoders.pkl')

print("Referral and promo fraud detection model trained and saved.")
