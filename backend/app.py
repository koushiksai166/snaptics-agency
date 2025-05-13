from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
import os

app = Flask(__name__)
CORS(app)  # Allows requests from different ports (like 5501)

@app.route('/send-email', methods=['POST'])
def send_email():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    subject = request.form['subject']
    message = request.form['message']

    email_subject = f"New message from {name} - {subject}"
    email_body = f"""
    Name: {name}
    Email: {email}
    Phone: {phone}
    Subject: {subject}
    Message: {message}
    """

    sender_email = "saikumar.dmm@snaptics.in"
    sender_password = "ldqc nlsf hkol hfvy"
    receiver_email = "saikumar.dmm@snaptics.in"

    msg = MIMEText(email_body)
    msg["Subject"] = email_subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        return jsonify({"status": "success", "message": "Email sent successfully!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use PORT from environment if available
    app.run(host='0.0.0.0', port=port, debug=True)
