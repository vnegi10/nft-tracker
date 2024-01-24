import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def set_colors(price_change):
    colors = ['red'] * len(price_change)

    for (index, change) in enumerate(price_change):
        if change > 0:
            colors[index] = 'green'

    return colors

def get_app_password():
    f = open("/home/vikas/Documents/Gmail_app_pass.json")
    pass_dict = json.load(f)
    return pass_dict["pass"]

def send_price_alert(to_email, subject, body):
    
    # Replace with your Gmail email address
    sender_email = 'nftdemoapp@gmail.com'
    
    # Replace with your Gmail app password
    sender_password = get_app_password()

    # Email content
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the body of the email
    msg.attach(MIMEText(body, 'plain'))

    # Establish a connection to the SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        
        # Send the email
        server.sendmail(sender_email, to_email, msg.as_string())