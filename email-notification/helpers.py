import os
from flask_mail import Message 
from dotenv import load_dotenv

load_dotenv() 

def send_personalized_email(mail):
    try:
        subject = 'Hello Joy'
        msg = Message(
            subject,
            sender=(os.getenv('MAIL_SENDER'), os.getenv('SENDER_MAIL_ID')),
            recipients=['joy.almeida@spit.ac.in']
        )
        msg.body = 'we noticed you raided a bank, here are some more things you can do...'
        mail.send(msg)
        print('Email sent successfully')
    except Exception as e:
        print(f'Failed to send email: {e}')