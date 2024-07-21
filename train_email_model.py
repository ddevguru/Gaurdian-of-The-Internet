import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

# Load dataset
data = pd.read_csv('email_content_dataset.csv')

# Feature and target variable
X = data['email_content']
y = data['label']

# Create a pipeline that combines a CountVectorizer with a Naive Bayes classifier
model = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', MultinomialNB())
])

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'email_content_detection_model.pkl')

print("Model trained and saved.")
