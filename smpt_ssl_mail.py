import smtplib, ssl, getpass

port = 465 # SSL port

sender_mail = "senshiramma@gmail.com"
receiver_mail = "senshiramma@gmail.com"
password = getpass.getpass("Input your password\n")
smtp_server = "smtp.gmail.com"

message = """\
Subject: Test


Hola, como va?!

This is an email sent using pythonSMTP
"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(receiver_mail, password)
    server.sendmail(sender_mail, receiver_mail, message)
