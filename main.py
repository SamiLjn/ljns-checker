import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os
from datetime import datetime
import checker

load_dotenv()

print("Checking d'API")

gmail_address = os.environ["GMAIL_ADDRESS"]
gmail_password = os.environ["GMAIL_PWD_ACCOUNT"]
smtp_server = 'smtp.gmail.com'
smtp_port = 587

today_date = datetime.now().strftime("%d %B %Y")

blog_e_sport_active = checker.check_blog_esport_api_status()
bropoll_active = checker.check_bropoll_api_status()
todo_active = checker.check_todo_api_status()

# Création de l'e-mail
msg = MIMEMultipart()
msg['From'] = gmail_address
msg['To'] = gmail_address
msg['Subject'] = 'API checker'

body = f"""
Ton daily checker du {today_date} des APIs :

- BLOG E-SPORT : {'actif' if blog_e_sport_active else 'inactif'}
- BROPOLL : {'actif' if bropoll_active else 'inactif'}
- TODO : {'actif' if todo_active else 'inactif'}
"""
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(gmail_address, gmail_password)

server.send_message(msg)

server.quit()
print('Email envoyé le sang')
