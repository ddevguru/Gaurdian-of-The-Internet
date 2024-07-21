import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
data = pd.read_csv('url_data.csv')

# Features and target
X = data[['length', 'has_ip', 'has_at', 'num_hyphens', 'num_dots', 'has_https']]
y = data['is_fraud']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'url_fraud_detection_model.pkl')

print("URL fraud detection model trained and saved.")
