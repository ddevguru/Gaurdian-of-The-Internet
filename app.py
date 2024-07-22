from flask import Flask, render_template, redirect, url_for, request, flash, session
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
# Load models and encoders
email_model = joblib.load('email_content_detection_model.pkl')
sms_model = joblib.load('sms_fraud_detection_model.pkl')
insurance_model = joblib.load('insurance_fraud_detection_model.pkl')
credit_card_model = joblib.load('credit_card_fraud_detection_model.pkl')
credit_card_encoders = joblib.load('label_encoders.pkl')
gift_card_model = joblib.load('gift_card_fraud_detection_model.pkl')
gift_card_encoders = joblib.load('gift_card_label_encoders.pkl')
charity_fund_model = joblib.load('charity_fund_fraud_detection_model.pkl')
charity_fund_encoders = joblib.load('charity_fund_label_encoders.pkl')
otp_model = joblib.load('otp_fraud_detection_model.pkl')
otp_encoders = joblib.load('otp_label_encoders.pkl')
url_model = joblib.load('url_fraud_detection_model.pkl')
ad_model = joblib.load('ad_fraud_detection_model.pkl')
ad_encoders = joblib.load('ad_label_encoders.pkl')
referral_promo_model = joblib.load('referral_promo_fraud_detection_model.pkl')
referral_promo_encoders = joblib.load('referral_promo_label_encoders.pkl')

# Load the model for predictions
email_model = joblib.load('email_content_detection_model.pkl')

def detect_fake_email(emailcontent):
    prediction = email_model.predict([emailcontent])
    print(f"Email Content: {emailcontent}, Prediction: {prediction[0]}")
    return "Fake email detected" if prediction[0] == 'fake' else "Genuine email"

def detect_fraud_sms(message):
    prediction = sms_model.predict([message])
    print(f"Message: {message}, Prediction: {prediction[0]}")
    return "Fraudulent SMS detected" if prediction[0] == 'fraudulent' else "Genuine SMS"

def detect_fraud_insurance(description):
    prediction = insurance_model.predict([description])
    print(f"Insurance Description: {description}, Prediction: {prediction[0]}")
    return "Fraudulent claim detected" if prediction[0] == 'fraudulent' else "Genuine claim"

def detect_fraud_credit_card(amount, user_id, merchant_id, location):
    data = pd.DataFrame([[amount, user_id, merchant_id, location]], columns=['amount', 'user_id', 'merchant_id', 'location'])
    for column in ['merchant_id', 'location']:
        data[column] = credit_card_encoders[column].transform(data[column])
    prediction = credit_card_model.predict(data)
    print(f"Credit Card Data: {data}, Prediction: {prediction[0]}")
    return "Fraudulent" if prediction[0] == 1 else "Genuine"

def detect_fraud_gift_card(amount, user_id, merchant_id, location, gift_card_type):
    data = pd.DataFrame([[amount, user_id, merchant_id, location, gift_card_type]], columns=['amount', 'user_id', 'merchant_id', 'location', 'gift_card_type'])
    for column in ['merchant_id', 'location', 'gift_card_type']:
        data[column] = gift_card_encoders[column].transform(data[column])
    prediction = gift_card_model.predict(data)
    print(f"Gift Card Data: {data}, Prediction: {prediction[0]}")
    return "Fraudulent" if prediction[0] == 1 else "Genuine"

def detect_fraud_charity_fund(amount, user_id, charity_id, location, donation_type):
    data = pd.DataFrame([[amount, user_id, charity_id, location, donation_type]], columns=['amount', 'user_id', 'charity_id', 'location', 'donation_type'])
    for column in ['charity_id', 'location', 'donation_type']:
        data[column] = charity_fund_encoders[column].transform(data[column])
    prediction = charity_fund_model.predict(data)
    print(f"Charity Fund Data: {data}, Prediction: {prediction[0]}")
    return "Fraudulent" if prediction[0] == 1 else "Genuine"

def detect_fraud_otp(amount, user_id, phone_number, location, otp_type):
    data = pd.DataFrame([[amount, user_id, phone_number, location, otp_type]], columns=['amount', 'user_id', 'phone_number', 'location', 'otp_type'])
    for column in ['phone_number', 'location', 'otp_type']:
        data[column] = otp_encoders[column].transform(data[column])
    prediction = otp_model.predict(data)
    print(f"OTP Data: {data}, Prediction: {prediction[0]}")
    return "Fraudulent" if prediction[0] == 1 else "Genuine"

def detect_fraud_url(url):
    length = len(url)
    has_ip = 1 if any(char.isdigit() for char in url.split('.')[0]) else 0
    has_at = 1 if '@' in url else 0
    num_hyphens = url.count('-')
    num_dots = url.count('.')
    has_https = 1 if url.startswith('https://') else 0
    data = pd.DataFrame([[length, has_ip, has_at, num_hyphens, num_dots, has_https]], columns=['length', 'has_ip', 'has_at', 'num_hyphens', 'num_dots', 'has_https'])
    prediction = url_model.predict(data)
    print(f"URL: {url}, Prediction: {prediction[0]}")
    return "Fraudulent" if prediction[0] == 1 else "Genuine"

def detect_fraud_ad(clicks, impressions, country, browser, ad_platform):
    data = pd.DataFrame([[clicks, impressions, country, browser, ad_platform]], columns=['clicks', 'impressions', 'country', 'browser', 'ad_platform'])
    data['country'] = ad_encoders['country'].transform(data['country'])
    data['browser'] = ad_encoders['browser'].transform(data['browser'])
    prediction = ad_model.predict(data)
    print(f"Ad Data: {data}, Prediction: {prediction[0]}")
    return "Fraudulent" if prediction[0] == 1 else "Genuine"

def detect_fraud_referral_promo(promo_code, num_referrals, total_spent):
    try:
        num_referrals = int(num_referrals)
        total_spent = float(total_spent)
    except ValueError:
        return "Invalid input. Please enter valid numerical values for referrals and total spent."

    if num_referrals > 10:
        return "Suspicious activity detected"
    if total_spent > 1000 and promo_code.startswith("FRAUD"):
        return "Fraud detected"
    return "No fraud detected"


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
                cursor.execute('INSERT INTO users (name, username, email, phonenumber, password) VALUES (%s, %s, %s, %s, %s)', (name, username, email, phonenumber, password))
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
    return redirect(url_for('signin'))

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form.get('phone')
        message = request.form['message']
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO user_details (name, email, phone, message) VALUES (%s, %s, %s, %s)', (name, email, phone, message))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('success'))
    return render_template('contactus.html')

@app.route('/success')
def success():
    return render_template('success.html')


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


@app.route('/email-fraud', methods=['GET', 'POST'])
def email_fraud():
    if 'loggedin' in session:
        if request.method == 'POST':
            emailcontent = request.form['emailcontent']
            result = detect_fake_email(emailcontent)
            cursor = mysql.connection.cursor()
            cursor.execute('INSERT INTO email_submissions (emailcontent, result) VALUES (%s, %s)', (emailcontent, result))
            mysql.connection.commit()
            cursor.close()
            return redirect(url_for('emailresult', emailcontent=emailcontent, result=result))
        return render_template('phishing.html')
    return redirect(url_for('signin'))

@app.route('/emailresult')
def emailresult():
    results = request.args.get('results')
    
    # Fetch all email submissions
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM email_submissions')
    submissions = cursor.fetchall()
    
    return render_template('emailresults.html', results=results, submissions=submissions)

@app.route('/sms-fraud', methods=['GET', 'POST'])
def sms_fraud():
    if 'loggedin' in session:
        if request.method == 'POST':
            message = request.form['message']
            result = detect_fraud_sms(message)
            cursor = mysql.connection.cursor()
            cursor.execute('INSERT INTO sms_submissions (sms_message, result) VALUES (%s, %s)', (message, result))
            mysql.connection.commit()
            cursor.close()
            return redirect(url_for('smsresult', message=message, result=result))
        return render_template('sms.html')
    return redirect(url_for('signin'))



@app.route('/smsresult')
def smsresult():
    sms = request.args.get('result')
    
    # Fetch all SMS submissions
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM sms_submissions')
    submissions = cursor.fetchall()
    
    return render_template('smsresult.html', sms=sms, submissions=submissions)



@app.route('/insurance-fraud', methods=['GET', 'POST'])
def insurance_fraud():
    if 'loggedin' in session:
        if request.method == 'POST':
            description = request.form['description']
            result = detect_fraud_insurance(description)
            cursor = mysql.connection.cursor()
            cursor.execute('INSERT INTO insurance_claims (claim_description, result) VALUES (%s, %s)', (description, result))
            mysql.connection.commit()
            cursor.close()
            return render_template('insuranceresult.html', description=description, result=result)
        return render_template('insurance.html')
    return redirect(url_for('signin'))


@app.route('/insuranceresult')
def insuranceresult():
    result = request.args.get('result')
    
    # Fetch all claims from the database
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM insurance_claims')
    claims = cursor.fetchall()
    
    return render_template('insuranceresult.html', result=result, claims=claims)


@app.route('/credit-card-fraud', methods=['GET', 'POST'])
def credit_card_fraud():
    if 'loggedin' in session:
        if request.method == 'POST':
            amount = request.form['amount']
            user_id = request.form['user_id']
            merchant_id = request.form['merchant_id']
            location = request.form['location']
            result = detect_fraud_credit_card(amount, user_id, merchant_id, location)
            cursor = mysql.connection.cursor()
            cursor.execute('INSERT INTO credit_card_transactions (amount, user_id, merchant_id, location, result) VALUES (%s, %s, %s, %s, %s)', (amount, user_id, merchant_id, location, result))
            mysql.connection.commit()
            cursor.close()
            return render_template('result_credit_card.html', amount=amount, user_id=user_id, merchant_id=merchant_id, location=location, result=result)
        return render_template('/creditfraud.html')
    return redirect(url_for('signin'))

@app.route('/result_credit_card')
def result_credit_card():
    result = request.args.get('result')
    
    # Fetch all credit card transactions
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM credit_card_transactions')
    transactions = cursor.fetchall()
    
    return render_template('result_credit_card.html', result=result, transactions=transactions)


@app.route('/gift-card-fraud', methods=['GET', 'POST'])
def gift_card_fraud():
    if 'loggedin' in session:
        if request.method == 'POST':
            amount = request.form['amount']
            user_id = request.form['user_id']
            merchant_id = request.form['merchant_id']
            location = request.form['location']
            gift_card_type = request.form['gift_card_type']
            result = detect_fraud_gift_card(amount, user_id, merchant_id, location, gift_card_type)
            cursor = mysql.connection.cursor()
            cursor.execute('INSERT INTO gift_card_transactions (amount, user_id, merchant_id, location, gift_card_type, result) VALUES (%s, %s, %s, %s, %s, %s)', (amount, user_id, merchant_id, location, gift_card_type, result))
            mysql.connection.commit()
            cursor.close()
            return render_template('result_gift_card.html', amount=amount, user_id=user_id, merchant_id=merchant_id, location=location, gift_card_type=gift_card_type, result=result)
        return render_template('giftcard.html')
    return redirect(url_for('signin'))


@app.route('/result_gift_card')
def result_gift_card():
    result = request.args.get('result')
    
    # Fetch all gift card transactions
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM gift_card_transactions')
    transactions = cursor.fetchall()
    
    return render_template('result_gift_card.html', result=result, transactions=transactions)


@app.route('/charity-fund-fraud', methods=['GET', 'POST'])
def charity_fund_fraud():
    if 'loggedin' in session:
        if request.method == 'POST':
            amount = request.form['amount']
            user_id = request.form['user_id']
            charity_id = request.form['charity_id']
            location = request.form['location']
            donation_type = request.form['donation_type']
            result = detect_fraud_charity_fund(amount, user_id, charity_id, location, donation_type)
            cursor = mysql.connection.cursor()
            cursor.execute('INSERT INTO charity_fund_transactions (amount, user_id, charity_id, location, donation_type, result) VALUES (%s, %s, %s, %s, %s, %s)', (amount, user_id, charity_id, location, donation_type, result))
            mysql.connection.commit()
            cursor.close()
            return render_template('result_charity_fund.html', amount=amount, user_id=user_id, charity_id=charity_id, location=location, donation_type=donation_type, result=result)
        return render_template('charityfraud.html')
    return redirect(url_for('signin'))

@app.route('/result_charity_fund')
def result_charity_fund():
    result = request.args.get('result')
    
    # Fetch all charity fund transactions
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM charity_fund_transactions')
    transactions = cursor.fetchall()
    
    return render_template('result_charity_fund.html', result=result, transactions=transactions)

@app.route('/otp-fraud', methods=['GET', 'POST'])
def otp_fraud():
    if 'loggedin' in session:
        if request.method == 'POST':
            amount = request.form['amount']
            user_id = request.form['user_id']
            phone_number = request.form['phone_number']
            location = request.form['location']
            otp_type = request.form['otp_type']
            result = detect_fraud_otp(amount, user_id, phone_number, location, otp_type)
            cursor = mysql.connection.cursor()
            cursor.execute('INSERT INTO otp_transactions (amount, user_id, phone_number, location, otp_type, result) VALUES (%s, %s, %s, %s, %s, %s)', (amount, user_id, phone_number, location, otp_type, result))
            mysql.connection.commit()
            cursor.close()
            return render_template('result_otp.html', amount=amount, user_id=user_id, phone_number=phone_number, location=location, otp_type=otp_type, result=result)
        return render_template('fakeotp.html')
    return redirect(url_for('signin'))


@app.route('/result_otp')
def result_otp():
    result = request.args.get('result')
    
    # Fetch all OTP transactions
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM otp_transactions')
    transactions = cursor.fetchall()
    
    return render_template('result_otp.html', result=result, transactions=transactions)



@app.route('/url-fraud', methods=['GET', 'POST'])
def url_fraud():
    if 'loggedin' in session:
        if request.method == 'POST':
            url = request.form['url']
            result = detect_fraud_url(url)
            cursor = mysql.connection.cursor()
            cursor.execute('INSERT INTO url_transactions (url, result) VALUES (%s, %s)', (url, result))
            mysql.connection.commit()
            cursor.close()
            return redirect(url_for('result_url', url=url, result=result))
        return render_template('fakesite.html')
    return redirect(url_for('signin'))

@app.route('/result_url')
def result_url():
    result = request.args.get('result')
    
    # Fetch all URL transactions
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM url_transactions')
    transactions = cursor.fetchall()
    
    return render_template('result_url.html', result=result, transactions=transactions)

@app.route('/ad-fraud', methods=['GET', 'POST'])
def ad_fraud():
    if 'loggedin' in session:
        if request.method == 'POST':
            clicks = request.form['clicks']
            impressions = request.form['impressions']
            country = request.form['country']
            browser = request.form['browser']
            ad_platform = request.form['ad_platform']
            result = detect_fraud_ad(clicks, impressions, country, browser, ad_platform)
            cursor = mysql.connection.cursor()
            cursor.execute('INSERT INTO ad_transactions (clicks, impressions, country, browser, result) VALUES (%s, %s, %s, %s, %s)', (clicks, impressions, country, browser, result))
            mysql.connection.commit()
            cursor.close()
            return render_template('result_ad.html', clicks=clicks, impressions=impressions, country=country, browser=browser, result=result)
        return render_template('ad.html')
    return redirect(url_for('signin'))

@app.route('/result_ad')
def result_ad():
    result = request.args.get('result')
    
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM ad_transactions')
    transactions = cursor.fetchall()
    
    return render_template('result_ad.html', result=result, transactions=transactions)

@app.route('/referral-promo-fraud', methods=['GET', 'POST'])
def referral_promo_fraud():
    if 'loggedin' in session:
        if request.method == 'POST':
            promo_code = request.form['promo_code']
            num_referrals = request.form['num_referrals']
            total_spent = request.form['total_spent']
            result = detect_fraud_referral_promo(promo_code, num_referrals, total_spent)
            cursor = mysql.connection.cursor()
            cursor.execute('INSERT INTO referral_promo_transactions (promo_code, num_referrals, total_spent, result) VALUES (%s, %s, %s, %s)', (promo_code, num_referrals, total_spent, result))
            mysql.connection.commit()
            cursor.close()
            return render_template('result_referral_promo.html', promo_code=promo_code, num_referrals=num_referrals, total_spent=total_spent, result=result)
        return render_template('referral.html')
    return redirect(url_for('signin'))

@app.route('/result_referral_promo')
def result_referral_promo():
    result = request.args.get('result')
    
    # Fetch all referral and promo transactions
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM referral_promo_transactions')
    transactions = cursor.fetchall()
    
    return render_template('result_referral_promo.html', result=result, transactions=transactions)

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('signin'))

if __name__ == '__main__':
    app.run(debug=True)
