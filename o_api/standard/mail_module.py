import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

port = 587
smtp_server = 'smtp.gmail.com'
sender_email = 'uj06134@gmail.com'
receiver_email = 'uj06134@gmail.com'
password = 'tvhy effs ktiz xomi'
message = '<h1>내용</h1>'

msg = MIMEText(message, 'html')
data = MIMEMultipart()
data.attach(msg)

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, data.as_string())