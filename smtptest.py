# -*- coding: utf-8 -*-
#!/usr/bin/env python
#
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.image import MIMEImage

import smtplib
import string

HOST = "smtp.163.com"
SUBJECT = "Tesr email from Python"
TO = "testmail@163.com"
FROM = "testmail@163.com"
text = "python test smtp"
BODY = string.join((
    "From : %s"% FROM,
    "To: %s"% TO,
    "Subject: %s"% SUBJECT,
    '',
    text
),"\r\n")

server = smtplib.SMTP()
server.connect(HOST,'25')
server.starttls()
server.login("testmail@163.com","password")
server.sendmail(FROM, [TO], BODY)
server.quit()