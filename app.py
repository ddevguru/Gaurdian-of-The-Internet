from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo
from flask_mysqldb import MySQL
import MySQLdb.cursors
from fraud_detection import detect_fraud 
import joblib
import pandas as pd

app = Flask(__name__)
app.secret_key = 'fraud@123'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'kuchbhi'

mysql = MySQL(app)

# Load the trained model
model = joblib.load('email_content_detection_model.pkl')

def detect_fake_email(content):
    prediction = model.predict([content])
    if prediction[0] == 'fake':
        return "Fake email detected"
    return "Genuine email"

model = joblib.load('sms_fraud_detection_model.pkl')

def detect_fraud(message):
    prediction = model.predict([message])
    if prediction[0] == 'fraudulent':
        return "Fraudulent SMS detected"
    return "Genuine SMS"


model = joblib.load('insurance_fraud_detection_model.pkl')

def detect_fraud(description):
    prediction = model.predict([description])
    if prediction[0] == 'fraudulent':
        return "Fraudulent claim detected"
    return "Genuine claim"



# Load models and label encoders
model = joblib.load('credit_card_fraud_detection_model.pkl')
label_encoders = joblib.load('label_encoders.pkl')

def detect_fraud(amount, user_id, merchant_id, location):
    # Prepare input data
    data = pd.DataFrame([[amount, user_id, merchant_id, location]], columns=['amount', 'user_id', 'merchant_id', 'location'])
    
    # Encode categorical features
    for column in ['merchant_id', 'location']:
        data[column] = label_encoders[column].transform(data[column])
    
    # Predict fraud
    prediction = model.predict(data)
    return "Fraudulent" if prediction[0] == 1 else "Genuine"


# Load models and label encoders
model = joblib.load('gift_card_fraud_detection_model.pkl')
label_encoders = joblib.load('gift_card_label_encoders.pkl')

def detect_fraud(amount, user_id, merchant_id, location, gift_card_type):
    # Prepare input data
    data = pd.DataFrame([[amount, user_id, merchant_id, location, gift_card_type]], columns=['amount', 'user_id', 'merchant_id', 'location', 'gift_card_type'])
    
    # Encode categorical features
    for column in ['merchant_id', 'location', 'gift_card_type']:
        data[column] = label_encoders[column].transform(data[column])
    
    # Predict fraud
    prediction = model.predict(data)
    return "Fraudulent" if prediction[0] == 1 else "Genuine"

# Load models and label encoders
model = joblib.load('charity_fund_fraud_detection_model.pkl')
label_encoders = joblib.load('charity_fund_label_encoders.pkl')

def detect_fraud(amount, user_id, charity_id, location, donation_type):
    # Prepare input data
    data = pd.DataFrame([[amount, user_id, charity_id, location, donation_type]], columns=['amount', 'user_id', 'charity_id', 'location', 'donation_type'])
    
    # Encode categorical features
    for column in ['charity_id', 'location', 'donation_type']:
        data[column] = label_encoders[column].transform(data[column])
    
    # Predict fraud
    prediction = model.predict(data)
    return "Fraudulent" if prediction[0] == 1 else "Genuine"



# Load models and label encoders
model = joblib.load('otp_fraud_detection_model.pkl')
label_encoders = joblib.load('otp_label_encoders.pkl')

def detect_fraud(amount, user_id, phone_number, location, otp_type):
    # Prepare input data
    data = pd.DataFrame([[amount, user_id, phone_number, location, otp_type]], columns=['amount', 'user_id', 'phone_number', 'location', 'otp_type'])
    
    # Encode categorical features
    for column in ['phone_number', 'location', 'otp_type']:
        data[column] = label_encoders[column].transform(data[column])
    
    # Predict fraud
    prediction = model.predict(data)
    return "Fraudulent" if prediction[0] == 1 else "Genuine"

# Load model
model = joblib.load('url_fraud_detection_model.pkl')

def detect_fraud(url):
    # Feature extraction from URL
    length = len(url)
    has_ip = 1 if any(char.isdigit() for char in url.split('.')[0]) else 0
    has_at = 1 if '@' in url else 0
    num_hyphens = url.count('-')
    num_dots = url.count('.')
    has_https = 1 if url.startswith('https://') else 0

    # Prepare input data
    data = pd.DataFrame([[length, has_ip, has_at, num_hyphens, num_dots, has_https]], columns=['length', 'has_ip', 'has_at', 'num_hyphens', 'num_dots', 'has_https'])
    
    # Predict fraud
    prediction = model.predict(data)
    return "Fraudulent" if prediction[0] == 1 else "Genuine"


# Load model and label encoders
model = joblib.load('ad_fraud_detection_model.pkl')
label_encoders = joblib.load('ad_label_encoders.pkl')

def detect_fraud(ad_platform, clicks, impressions, country, browser):
    # Prepare input data
    data = pd.DataFrame([[ad_platform, clicks, impressions, country, browser]],
                        columns=['ad_platform', 'clicks', 'impressions', 'country', 'browser'])
    
    # Encode categorical features
    for column in ['ad_platform', 'country', 'browser']:
        data[column] = label_encoders[column].transform(data[column])
    
    # Predict fraud
    prediction = model.predict(data)
    return "Fraudulent" if prediction[0] == 1 else "Genuine"

# Load model and label encoders
model = joblib.load('referral_promo_fraud_detection_model.pkl')
label_encoders = joblib.load('referral_promo_label_encoders.pkl')

def detect_fraud(referral_code, promo_code, num_referrals, total_spent):
    # Prepare input data
    data = pd.DataFrame([[referral_code, promo_code, num_referrals, total_spent]],
                        columns=['referral_code', 'promo_code', 'num_referrals', 'total_spent'])
    
    # Encode categorical features
    for column in ['referral_code', 'promo_code']:
        data[column] = label_encoders[column].transform(data[column])
    
    # Predict fraud
    prediction = model.predict(data)
    return "Fraudulent" if prediction[0] == 1 else "Genuine"




@app.route('/')
def index():
    return render_template('index.html')


@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/afterloginaboutus')
def afterloginaboutus():
    return render_template('afterloginaboutus.html')



@app.route('/about')
def about():
    return render_template('about1.html')
@app.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        email = request.form['email']
        phonenumber = request.form['phonenumber']
        password = request.form['password']
        confirm_password = request.form['cpassword']

        if password != confirm_password:
            flash('Passwords do not match!', 'danger')
        else:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
            account = cursor.fetchone()
            if account:
                flash('Username already exists!', 'danger')
            else:
                cursor.execute('INSERT INTO users (name,username, email, phonenumber, password) VALUES (%s, %s,%s,%s,%s)', (name, username, email, phonenumber, password))
                mysql.connection.commit()
                flash('You have successfully registered!', 'success')
                return redirect(url_for('signin'))
    return render_template('sign-up.html')

@app.route('/sign-in', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Incorrect username or password!', 'danger')
    return render_template('sign-in.html')

@app.route('/home')
def home():
    if 'loggedin' in session:
        return render_template('home.html')
    return redirect(url_for('login'))

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        
        name = request.form['name']
        email = request.form['email']
        phone = request.form.get('phone')  
        message = request.form['message']
        
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO user_details (name, email, phone, message) VALUES (%s, %s, %s, %s)', 
                       (name, email, phone, message))
        mysql.connection.commit()
        cursor.close()
        
        return redirect(url_for('success'))
    
    
    return render_template('contactus.html')

@app.route('/success')
def success():
    return "Thank you for your submission!"

@app.route('/logout')
def logout():
    session.pop('loggedin', None)   
    session.pop('id', None)
    session.pop('username', None)
    flash('You have successfully logged out!', 'success')
    return redirect(url_for('signin'))

@app.route('/investment', methods=['GET', 'POST'])
def investment():
    if 'loggedin' in session:
        if request.method == 'POST':
            data = request.form['data']
            result = detect_fraud(data)
            cursor = mysql.connection.cursor()
            cursor.execute('INSERT INTO user_submissions (user_id, data, result) VALUES (%s, %s, %s)', (session['id'], data, result))
            mysql.connection.commit()
            return redirect(url_for('result', result=result))
        return render_template('investment.html')
    return redirect('/login')

@app.route('/result')
def result():
    result = request.args.get('result')
    return render_template('result.html', result=result)


@app.route('/fakeemail', methods=['GET', 'POST'])
def fakeemail():
    if request.method == 'POST':
        emailcontent = request.form['emailcontent']
        results = detect_fake_email(emailcontent)
        
        # Insert email content and result into the database
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO email_submissions (emailcontent, result) VALUES (%s, %s)', (emailcontent, results))
        mysql.connection.commit()
        
        return redirect(url_for('emailresult', results=results))
    return render_template('phishing.html')

@app.route('/emailresult')
def emailresult():
    results = request.args.get('results')
    
    # Fetch all email submissions
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM email_submissions')
    submissions = cursor.fetchall()
    
    return render_template('emailresults.html', results=results, submissions=submissions)


@app.route('/sms', methods=['GET', 'POST'])
def sms():
    if request.method == 'POST':
        phone_number = request.form['phone_number']
        sms_message = request.form['sms_message']
        sms = detect_fraud(sms_message)
        
        # Insert SMS message and result into the database
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO sms_submissions (phone_number,sms_message, result) VALUES (%s, %s, %s)', (phone_number, sms_message, sms))
        mysql.connection.commit()
        
        return redirect(url_for('smsresult', sms=sms))
    return render_template('sms.html')

@app.route('/smsresult')
def smsresult():
    sms = request.args.get('sms')
    
    # Fetch all SMS submissions
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM sms_submissions')
    submissions = cursor.fetchall()
    
    return render_template('smsresult.html', sms=sms, submissions=submissions)


@app.route('/insurance', methods=['GET', 'POST'])
def insurance():
    if request.method == 'POST':
        claimant_name = request.form['claimant_name']
        claim_amount = request.form['claim_amount']
        claim_description = request.form['claim_description']
        claim_date = request.form['claim_date']
        
        result = detect_fraud(claim_description)
        
        # Insert claim details and result into the database
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO insurance_claims (claimant_name, claim_amount, claim_description, claim_date, result) VALUES (%s, %s, %s, %s, %s)', (claimant_name, claim_amount, claim_description, claim_date, result))
        mysql.connection.commit()
        
        return redirect(url_for('insuranceresult', result=result))
    return render_template('insurance.html')

@app.route('/insuranceresult')
def insuranceresult():
    result = request.args.get('result')
    
    # Fetch all claims from the database
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM insurance_claims')
    claims = cursor.fetchall()
    
    return render_template('insuranceresult.html', result=result, claims=claims)

@app.route('/submit_credit_card', methods=['GET', 'POST'])
def submit_credit_card():
    if request.method == 'POST':
        amount = float(request.form['amount'])
        user_id = int(request.form['user_id'])
        merchant_id = request.form['merchant_id']
        location = request.form['location']
        
        result = detect_fraud(amount, user_id, merchant_id, location)
        
        # Insert credit card transaction details and result into the database
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO credit_card_transactions (amount, user_id, merchant_id, location, result) VALUES (%s, %s, %s, %s, %s)', (amount, user_id, merchant_id, location, result))
        mysql.connection.commit()
        
        return redirect(url_for('result_credit_card', result=result))
    return render_template('creditfraud.html')

@app.route('/result_credit_card')
def result_credit_card():
    result = request.args.get('result')
    
    # Fetch all credit card transactions
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM credit_card_transactions')
    transactions = cursor.fetchall()
    
    return render_template('result_credit_card.html', result=result, transactions=transactions)


@app.route('/submit_gift_card', methods=['GET', 'POST'])
def submit_gift_card():
    if request.method == 'POST':
        amount = float(request.form['amount'])
        user_id = int(request.form['user_id'])
        merchant_id = request.form['merchant_id']
        location = request.form['location']
        gift_card_type = request.form['gift_card_type']
        
        result = detect_fraud(amount, user_id, merchant_id, location, gift_card_type)
        
        # Insert gift card transaction details and result into the database
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO gift_card_transactions (amount, user_id, merchant_id, location, gift_card_type, result) VALUES (%s, %s, %s, %s, %s, %s)', (amount, user_id, merchant_id, location, gift_card_type, result))
        mysql.connection.commit()
        
        return redirect(url_for('result_gift_card', result=result))
    return render_template('giftcard.html')

@app.route('/result_gift_card')
def result_gift_card():
    result = request.args.get('result')
    
    # Fetch all gift card transactions
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM gift_card_transactions')
    transactions = cursor.fetchall()
    
    return render_template('result_gift_card.html', result=result, transactions=transactions)

@app.route('/submit_charity_fund', methods=['GET', 'POST'])
def submit_charity_fund():
    if request.method == 'POST':
        amount = float(request.form['amount'])
        user_id = int(request.form['user_id'])
        charity_id = request.form['charity_id']
        location = request.form['location']
        donation_type = request.form['donation_type']
        
        result = detect_fraud(amount, user_id, charity_id, location, donation_type)
        
        # Insert charity fund transaction details and result into the database
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO charity_fund_transactions (amount, user_id, charity_id, location, donation_type, result) VALUES (%s, %s, %s, %s, %s, %s)', (amount, user_id, charity_id, location, donation_type, result))
        mysql.connection.commit()
        
        return redirect(url_for('result_charity_fund', result=result))
    return render_template('charityfraud.html')

@app.route('/result_charity_fund')
def result_charity_fund():
    result = request.args.get('result')
    
    # Fetch all charity fund transactions
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM charity_fund_transactions')
    transactions = cursor.fetchall()
    
    return render_template('result_charity_fund.html', result=result, transactions=transactions)


@app.route('/submit_otp', methods=['GET', 'POST'])
def submit_otp():
    if request.method == 'POST':
        amount = float(request.form['amount'])
        user_id = int(request.form['user_id'])
        phone_number = request.form['phone_number']
        location = request.form['location']
        otp_type = request.form['otp_type']
        
        result = detect_fraud(amount, user_id, phone_number, location, otp_type)
        
        # Insert OTP transaction details and result into the database
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO otp_transactions (amount, user_id, phone_number, location, otp_type, result) VALUES (%s, %s, %s, %s, %s, %s)', (amount, user_id, phone_number, location, otp_type, result))
        mysql.connection.commit()
        
        return redirect(url_for('result_otp', result=result))
    return render_template('fakeotp.html')

@app.route('/result_otp')
def result_otp():
    result = request.args.get('result')
    
    # Fetch all OTP transactions
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM otp_transactions')
    transactions = cursor.fetchall()
    
    return render_template('result_otp.html', result=result, transactions=transactions)


@app.route('/submit_url', methods=['GET', 'POST'])
def submit_url():
    if request.method == 'POST':
        url = request.form['url']
        
        result = detect_fraud(url)
        
        # Insert URL details and result into the database
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO url_transactions (url, result) VALUES (%s, %s)', (url, result))
        mysql.connection.commit()
        
        return redirect(url_for('result_url', result=result))
    return render_template('fakesite.html')

@app.route('/result_url')
def result_url():
    result = request.args.get('result')
    
    # Fetch all URL transactions
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM url_transactions')
    transactions = cursor.fetchall()
    
    return render_template('result_url.html', result=result, transactions=transactions)

@app.route('/submit_ad', methods=['GET', 'POST'])
def submit_ad():
    if request.method == 'POST':
        ad_platform = request.form['ad_platform']
        clicks = int(request.form['clicks'])
        impressions = int(request.form['impressions'])
        country = request.form['country']
        browser = request.form['browser']
        
        result = detect_fraud(ad_platform, clicks, impressions, country, browser)
        
        # Insert ad details and result into the database
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO ad_transactions (ad_platform, clicks, impressions, country, browser, result) VALUES (%s, %s, %s, %s, %s, %s)', 
                       (ad_platform, clicks, impressions, country, browser, result))
        mysql.connection.commit()
        
        return redirect(url_for('result_ad', result=result))
    return render_template('ad.html')

@app.route('/result_ad')
def result_ad():
    result = request.args.get('result')
    
    # Fetch all ad transactions
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM ad_transactions')
    transactions = cursor.fetchall()
    
    return render_template('result_ad.html', result=result, transactions=transactions)

@app.route('/submit_referral_promo', methods=['GET', 'POST'])
def submit_referral_promo():
    if request.method == 'POST':
        referral_code = request.form['referral_code']
        promo_code = request.form['promo_code']
        num_referrals = int(request.form['num_referrals'])
        total_spent = float(request.form['total_spent'])
        
        result = detect_fraud(referral_code, promo_code, num_referrals, total_spent)
        
        # Insert details and result into the database
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO referral_promo_transactions (referral_code, promo_code, num_referrals, total_spent, result) VALUES (%s, %s, %s, %s, %s)', 
                       (referral_code, promo_code, num_referrals, total_spent, result))
        mysql.connection.commit()
        
        return redirect(url_for('result_referral_promo', result=result))
    return render_template('referral.html')

@app.route('/result_referral_promo')
def result_referral_promo():
    result = request.args.get('result')
    
    # Fetch all referral and promo transactions
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM referral_promo_transactions')
    transactions = cursor.fetchall()
    
    return render_template('result_referral_promo.html', result=result, transactions=transactions)


if __name__ == '__main__':
    app.run(debug=True)
