import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, recipient_email, subject, message):
    # Set up the SMTP server
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Create a message container
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject

    # Add the message body
    msg.attach(MIMEText(message, "plain"))

    try:
        # Log in to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)

        # Send the email
        server.send_message(msg)

        # Clean up the connection
        server.quit()

        print("Email sent successfully!")
    except Exception as e:
        print("An error occurred while sending the email:", str(e))

# Usage example
sender_email = "ah.sabbir108677@gmail.com"
sender_password = "your_password"
recipient_email = "kavacor715@vaband.com"
subject = "Hello from Python!"
message = "This is a test email sent from Python."

send_email(sender_email, sender_password, recipient_email, subject, message)
