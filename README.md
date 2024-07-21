# Gaurdian-of-The-Internet

Fraud Detection System
## Overview
This project is a comprehensive fraud detection system that identifies fraudulent activities across various domains including ad fraud, referral and promo abuse, fake emails, SMS scams, and more. The system leverages machine learning models to analyze data and detect potential fraud.

## Features

-**Ad Fraud Detection:** Identifies fraudulent ad transactions.
-**Referral and Promo Abuse Detection:** Detects misuse of referral codes and promotional offers.
-**Fake Email Detection:** Flags potentially fraudulent email addresses.
-**SMS Fraud Detection:**  Analyzes SMS content for signs of fraud.
-**Fake URL Detection:** Identifies potentially fraudulent URLs.
-**Gift Card Scam Detection:**  Flags suspicious gift card transactions.
-**Charity Fund Scam Detection:**  Detects fraudulent charity fund transactions.
-**Fake OTP Scam Detection:**  Identifies fraudulent OTP activities.
-**Fake Commercial Sites Detection:**  Flags suspicious commercial websites.
-**Credit Card Fraud Detection:**  Detects fraudulent credit card transactions.

## Technologies Used

-**Python:**  For machine learning and data processing.
-**Flask:**  Web framework for creating the web application.
-**MySQL:**  Database for storing transaction data.
-**Scikit-Learn:**  For building and training machine learning models.
-**Joblib:**  For saving and loading trained models.
-**HTML/CSS:**  For creating user interfaces.

## Dataset 

The dataset used for training the models was collected from YouData.ai. It includes various features relevant to detecting fraud in different domains.

## Setup

### 1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/fraud-detection-system.git
cd fraud-detection-system


### 2. **Install Dependencies**
Create a virtual environment and install the required packages.

```bash

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

3. Database Setup
Create the database and tables. Connect to MySQL and execute the SQL commands.

sql
Copy code
CREATE DATABASE fraud_detection;

USE fraud_detection;

CREATE TABLE ad_transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ad_platform VARCHAR(50),
    clicks INT,
    impressions INT,
    ip_address VARCHAR(50),
    country VARCHAR(50),
    browser VARCHAR(50),
    result VARCHAR(50),
    submission_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE referral_promo_transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    referral_code VARCHAR(50),
    promo_code VARCHAR(50),
    num_referrals INT,
    total_spent DECIMAL(10, 2),
    result VARCHAR(50),
    submission_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
4. Train the Models
Run the training scripts to create and save machine learning models.

bash
Copy code
python train_ad_fraud_model.py
python train_referral_promo_model.py
5. Run the Flask Application
Start the Flask web server.

bash
Copy code
python app.py
6. Access the Web Application
Open your browser and navigate to http://localhost:5000 to access the fraud detection system.

User Authentication
The web application includes user authentication with login and sign-in pages. Ensure you have a user management system in place, such as:

User Registration: Allows new users to sign up.
User Login: Authenticates existing users.
Session Management: Keeps users logged in during their session.
User Authentication Setup
Update Flask Configuration: Ensure the Flask app is configured for user authentication.
Database for Users: Create a table to store user credentials.
Example SQL for User Table:

sql
Copy code
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    password VARCHAR(255),
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
Integrate Authentication: Use libraries such as Flask-Login for session management.
Contributing
Feel free to contribute to this project by submitting pull requests or reporting issues.

License
This project is licensed under the MIT License.

Contact
For any questions or inquiries, please contact [your email address].


