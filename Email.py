import smtplib, ssl
import os

my_context = ssl.create_default_context()

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "enio2298@gmail.com"
    password = os.getenv("m")
    receiver = "enio2298@gmail.com"
    my_context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message.encode("utf8"))