import smtplib, ssl, getpass

smtp_server = 'smtp.gmail.com'
port = 587
sender_email = 'senshiramma@gmail.com'
receiver_email = 'senshiramma@gmail.com'

password = getpass.getpass("Enter your password\n")

message = """\
Subject: Prueba starttls


hola como va!!!
"""

# Create secure SSL context
context = ssl.create_default_context()

# Try to log in an send email
try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
except Exception as e:
    print(e)
finally:
    server.quit()
