import smtplib

port = 1025 # For localhost

message = "Test"
sender_email = "senshiramma@gmail.com"
receiver_email = "senshiramma@gmail.com"

with smtplib.SMTP("localhost", port) as server:
    server.sendmail(sender_email, receiver_email, message)
