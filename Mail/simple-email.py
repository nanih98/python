#! /usr/bin/python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os 

email = 'XXXXXXXXX'
password = 'XXXXXXXXXXXX'
send_to_email = 'XXXXXXXXXXXXX'
subject = 'This is the subject' # The subject line
message = "Hello world

msg = MIMEMultipart()
msg['From'] = email
msg['To'] = send_to_email
msg['Subject'] = subject

 # Attach the message to the MIMEMultipart object
msg.attach(MIMEText(message, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)
text = msg.as_string() # You now need to convert the MIMEMultipart object to a string to send
server.sendmail(email, send_to_email, text)
server.quit()
