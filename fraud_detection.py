import joblib

# Load the pre-trained model
model = joblib.load('fraud_detection_model.pkl')

def detect_fraud(data):
    prediction = model.predict([data])
    if prediction[0] == 1:
        return "Fraud detected"
    return "No fraud detected"
