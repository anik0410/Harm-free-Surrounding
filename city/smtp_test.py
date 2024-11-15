from email.message import EmailMessage
import ssl
import smtplib
import os

email_sender = os.environ.get('EMAIL_USER')  # Your email address
email_password = os.environ.get('EMAIL_PASS')  # Your app password

def send_test_email(email_receiver):
    subject = "Test Email"
    body = "This is a test email sent from the SMTP test script."

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
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    recipient_email = input("Enter the recipient's email: ")
    send_test_email(recipient_email)
