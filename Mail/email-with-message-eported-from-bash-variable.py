#!/usr/bin/python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

email = 'info@devopstech.org'
password = 'Info.12.96.13.@@'
send_to_email = 'info@devopstech.org'
subject = 'This is the subject' # The subject line
message = (os.environ["message"]) # need previously run the command $ export message 
# Example
# message="Hello world"
# export message (BUT RUN THE EXPORT COMMAND BEFORE YOU EXECUTE THIS SCRIPT)!!!!!


msg = MIMEMultipart()
msg['From'] = email
msg['To'] = send_to_email
msg['Subject'] = subject

 # Attach the message to the MIMEMultipart object
msg.attach(MIMEText(message, 'plain'))

server = smtplib.SMTP('smtp.ionos.es', 587)
server.starttls()
server.login(email, password)
text = msg.as_string() # You now need to convert the MIMEMultipart object to a string to send
server.sendmail(email, send_to_email, text)
server.quit()
