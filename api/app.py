from flask import Flask, render_template, request
from flask_mail import Mail, Message
import smtplib, ssl
import json
import os
app = Flask(__name__)

PROFILE_PATH = os.path.join("src\data")

# configuration of mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'ramavtar200797@gmail.com'
app.config['MAIL_PASSWORD'] = 'Pop(*)ty2025'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def index():
    profile = read_profile()
    print(profile)
    return render_template("index.html", context=profile)

def read_profile():
    print(PROFILE_PATH + "\profile.json")
    with open(PROFILE_PATH + "\profile.json") as proile:
        return json.loads(proile.read()) 


@app.route("/contact", methods=['GET', 'POST'] )    
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        msg = Message(
                        subject="Inquiry for software development",
                        body=f'Hi Ram' \
                        'You got a query from {name=} with mail {email}' \
                        'on context {subject}. find below message details:-' \
                        '{message}',
                        sender ='ramavtar200797@gmail.com',
                        recipients = ['vijay200797@gmail.com']
                    )
        # msg.body = 'Hello Flask message sent from Flask-Mail'
                
        mail.send(msg)

        # body=f'Hi Ram' \
        # 'You got a query from {name=} with mail {email}' \
        # 'on context {subject}. find below message details:-' \
        # '{message}',

        # context = ssl.create_default_context()
        # with smtplib.SMTP(app.config['MAIL_SERVER'], app.config['MAIL_PORT']) as server:
        #     server.ehlo()  # Can be omitted
        #     server.starttls(context=context)
        #     server.ehlo()  # Can be omitted
        #     server.login(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        #     server.sendmail(app.config['MAIL_USERNAME'], 'vijay200797@gmail.com', message)

        return "OK"

if __name__ == "__main__":
    app.run(host='https://portfolio-dev-ram-tech-app.vercel.app', port=5000, debug= True)