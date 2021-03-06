#! /usr/bin/python
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path

email = 'XXXXX'
password = 'XXXXXXXXXXXX'
send_to_email = 'XXXXXXXX'
subject = 'This is the subject'
message = 'This is my message'

#File location. 
#PREVIOUS COMMANDS FOR THIS TO WORK
# IMAGINE WE HAVE THIS VARIABLE SET TO:
# LOGFILE="/var/log/mycustomlog.log"
# THEN... I EXPORT THIS VARIABLE AND THEN PYTHON WILL CATCH IT
# export LOGFILE

file_location = (os.environ["LOGFILE"]) # the script will send an email with the logfile mycustomlog.log attached. 

msg = MIMEMultipart()
msg['From'] = email
msg['To'] = send_to_email
msg['Subject'] = subject

msg.attach(MIMEText(message, 'plain'))

# Setup the attachment
filename = os.path.basename(file_location)
attachment = open(file_location, "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

# Attach the attachment to the MIMEMultipart object
msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)
text = msg.as_string()
server.sendmail(email, send_to_email, text)
server.quit()
