import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
import joblib

# Load dataset
data = pd.read_csv('investment.csv')
X = data['text']  # Feature: text data
y = data['label']  # Target: 1 for fraud, 0 for not fraud

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a pipeline
pipeline = make_pipeline(
    TfidfVectorizer(),  # Convert text to numerical data
    LogisticRegression()  # Logistic Regression model
)

# Train the model
pipeline.fit(X_train, y_train)

# Save the model
joblib.dump(pipeline, 'fraud_detection_model.pkl')
