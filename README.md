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

The dataset used for training the models was collected from [YouData.ai](https://youdata.ai) It includes various features relevant to detecting fraud in different domains.
Following are some links of dataset:

[1](https://www.youdata.ai/m/datasets/662ddfb3ec1654669685710d)

[2](https://www.youdata.ai/m/datasets/64ddbbfbf4420f00091fb575)

[3](https://www.youdata.ai/m/datasets/661d142b4c40e249a48066ee)

[4](https://www.youdata.ai/m/datasets/662de3d4ec16546696857c2b)

[5](https://www.youdata.ai/m/datasets/662de2ee2edd02c265857a38)

[6](https://www.youdata.ai/m/datasets/661d15d9279aa8ef92326b3c)

## Setup

### 1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/fraud-detection-system.git
cd fraud-detection-system
```

### 2. **Install Dependencies**
Create a virtual environment and install the required packag

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```


### 3. **Install Libraries**
You can install all the dependencies listed in requirements.txt using the following command:

```sh
pip install -r requirements.txt
```

### 4. **Database Setup**
Create the database and tables. Connect to MySQL and execute the SQL commands.
Copy code

```sql

CREATE DATABASE kuchbhi;

USE kuchbhi;


CREATE TABLE `ad_transactions` (
  `id` int(11) NOT NULL,
  `ad_platform` varchar(50) DEFAULT NULL,
  `clicks` int(11) DEFAULT NULL,
  `impressions` int(11) DEFAULT NULL,
  `ip_address` varchar(50) DEFAULT NULL,
  `country` varchar(50) DEFAULT NULL,
  `browser` varchar(50) DEFAULT NULL,
  `result` varchar(50) DEFAULT NULL,
  `submission_time` timestamp NOT NULL DEFAULT current_timestamp()
);

CREATE TABLE `charity_fund_transactions` (
  `id` int(11) NOT NULL,
  `amount` decimal(10,2) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `charity_id` varchar(100) DEFAULT NULL,
  `location` varchar(100) DEFAULT NULL,
  `donation_type` varchar(100) DEFAULT NULL,
  `result` varchar(50) DEFAULT NULL,
  `submission_time` timestamp NOT NULL DEFAULT current_timestamp()
);

CREATE TABLE `credit_card_transactions` (
  `id` int(11) NOT NULL,
  `amount` decimal(10,2) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `merchant_id` varchar(100) DEFAULT NULL,
  `location` varchar(100) DEFAULT NULL,
  `result` varchar(50) DEFAULT NULL,
  `submission_time` timestamp NOT NULL DEFAULT current_timestamp()
);
CREATE TABLE `email_submissions` (
  `id` int(11) NOT NULL,
  `emailcontent` varchar(255) DEFAULT NULL,
  `result` varchar(255) DEFAULT NULL,
  `submission_time` timestamp NOT NULL DEFAULT current_timestamp()
);

CREATE TABLE `gift_card_transactions` (
  `id` int(11) NOT NULL,
  `amount` decimal(10,2) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `merchant_id` varchar(100) DEFAULT NULL,
  `location` varchar(100) DEFAULT NULL,
  `gift_card_type` varchar(100) DEFAULT NULL,
  `result` varchar(50) DEFAULT NULL,
  `submission_time` timestamp NOT NULL DEFAULT current_timestamp()
);



CREATE TABLE `insurance_claims` (
  `id` int(11) NOT NULL,
  `claimant_name` varchar(100) DEFAULT NULL,
  `claim_amount` decimal(10,2) DEFAULT NULL,
  `claim_description` text DEFAULT NULL,
  `claim_date` date DEFAULT NULL,
  `result` varchar(50) DEFAULT NULL,
  `submission_time` timestamp NOT NULL DEFAULT current_timestamp()
);

CREATE TABLE `otp_transactions` (
  `id` int(11) NOT NULL,
  `amount` decimal(10,2) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `phone_number` varchar(100) DEFAULT NULL,
  `location` varchar(100) DEFAULT NULL,
  `otp_type` varchar(100) DEFAULT NULL,
  `result` varchar(50) DEFAULT NULL,
  `submission_time` timestamp NOT NULL DEFAULT current_timestamp()
);

CREATE TABLE `referral_promo_transactions` (
  `id` int(11) NOT NULL,
  `referral_code` varchar(50) DEFAULT NULL,
  `promo_code` varchar(50) DEFAULT NULL,
  `num_referrals` int(11) DEFAULT NULL,
  `total_spent` decimal(10,2) DEFAULT NULL,
  `result` varchar(50) DEFAULT NULL,
  `submission_time` timestamp NOT NULL DEFAULT current_timestamp()
);


CREATE TABLE `sms_submissions` (
  `id` int(11) NOT NULL,
  `phone_number` varchar(50) NOT NULL,
  `sms_message` text NOT NULL,
  `result` varchar(50) NOT NULL,
  `submission_time` timestamp NOT NULL DEFAULT current_timestamp()
);




```

### 5. **Train the Models**
Run the training scripts to create and save machine learning models.

```bash

python train_ad_fraud_model.py
python train_charity_fund_model.py
python train_credit_card_model.py
python train_email_model.py
python train_gift_card_model.py
python train_insurance_model.py
python train_model.py
python train_otp_fraud_model.py
python train_referral_promo_model.py
python train_sms_model.py
python train_url_fraud_model.py
python fraud_detection.py

```

### 6. **Run the Flask Application**
Start the Flask web server.

```bash
python app.py
```

### 7. **Access the Web Application**

Open your browser and navigate to http://localhost:5000 to access the fraud detection system.

## User Authentication

The web application includes user authentication with login and sign-in pages. Ensure you have a user management system in place, such as:

-**User Registration:** Allows new users to sign up.

-**User Login:** Authenticates existing users.

-**Session Management:** Keeps users logged in during their session.

## User Authentication Setup

-**Update Flask Configuration:** Ensure the Flask app is configured for user authentication.

-**Database for Users:** Create a table to store user credentials.

## Example SQL for User Table:

```sql
Copy code
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    password VARCHAR(255),
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

Integrate Authentication: Use libraries such as Flask-Login for session management.

## Contributing 

Feel free to contribute to this project by submitting pull requests or reporting issues.

## License

This project is licensed under the MIT License.

## Contact

For any questions or inquiries, please contact 121deepak2104@sjcem.edu.in.


