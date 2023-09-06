import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender_email = 'awsomeaditya96@gmail.com'
recipient_email = 'pandeya_2@rknec.edu'
subject = 'Hello, Python Email!'
message = 'Hi,This is a test email sent from Python'

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = subject

msg.attach(MIMEText(message, 'plain'))

smtp_server = 'smtp.gmail.com'
smtp_port = 587

server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()

email_password = 'fferzcymdqjifpwm'
server.login(sender_email, email_password)

server.sendmail(sender_email, recipient_email, msg.as_string())

server.quit()
