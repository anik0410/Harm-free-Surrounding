from email.message import EmailMessage
import ssl
import smtplib
import os

# Set your email credentials using environment variables
email_sender = os.environ.get('EMAIL_USER')  # Your email address
email_password = os.environ.get('EMAIL_PASS')  # Your app password


def send_email(email_receiver, subject, body):
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
    except Exception as e:
        print(f"Error: {e}")
