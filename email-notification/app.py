import os
from flask import Flask
from flask_apscheduler import APScheduler

from flask_mail import Mail, Message 

from helpers import send_personalized_email

from dotenv import load_dotenv
load_dotenv() 

# set configuration values
class Config:
    SCHEDULER_API_ENABLED = True

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = os.getenv('MAIL_ID')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

# create app
app = Flask(__name__)
app.config.from_object(Config())

mail = Mail(app)

# initialize scheduler
scheduler = APScheduler()
scheduler.init_app(app)

# interval example
@scheduler.task('interval', id='job_personalized_mail', seconds=10)
def job_personalized_mail():
    with app.app_context():
        send_personalized_email(mail)

# @scheduler.task('cron', id='do_job_2', week='*', day_of_week='sun')
# def job2():
#     print('Job 3 executed')

if __name__ == '__main__':
    scheduler.start()
    app.run(debug=True)