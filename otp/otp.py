# Python program to generate OTP and send it via email
import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import Flask, request, render_template
from flask import redirect, url_for


app = Flask(__name__)

# Dictionary to store generated OTPs
otp_storage = {}

# Function to generate OTP
def generate_otp():
    return ''.join(random.choices('0123456789', k=6))

# Function to send OTP via email
def send_otp(receiver_email, otp):
    sender_email = "your email"  # Your email address
    sender_password = "your password"  # Your application-specific password

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = "OTP for Verification"

    body = f"Your OTP is: {otp}"
    message.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, sender_password)
        server.send_message(message)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send_otp", methods=["POST"])
def send_otp_route():
    email = request.form["email"]
    otp = generate_otp()
    send_otp(email, otp)
    otp_storage[email] = otp  # Store OTP in dictionary
    return redirect(url_for('index', email=email))

@app.route("/verify_otp", methods=["POST"])
def verify_otp():
    email = request.form["email_verify"]
    entered_otp = request.form["otp"]
    stored_otp = otp_storage.get(email)
    
    if stored_otp == entered_otp:
        return "<h2>OTP verification successful!</h2>"
    else:
        return "<h2>OTP verification failed. Please try again.</h2>"

if __name__ == "__main__":
    app.run(debug=True, port=5001)

