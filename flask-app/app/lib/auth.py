from os import environ
from flask_mail import Mail, Message
from flask import redirect, render_template
from flask_login import current_user
from app.models import User
from random import randrange
from datetime import datetime
from app import db
import threading
import time
import json

base_url = environ.get("BASE_URL")
vcode_sender = environ.get("VERIFICATION_EMAIL")

limit_domains = environ.get("LIMIT_REGISTRATION_DOMAINS")
valid_domains = open('app/email_domains.json')
domains = json.load(valid_domains)

# Return user object
def get_user():
    id = current_user.get_id()
    user = User.query.filter_by(id=id).first()
    return user

def send_email(app, message, redirect_url):
    mail= Mail(app)
    mail.send(message)
    return redirect(redirect_url)

# Reset user verification code after 10 minutes
def verification_timeout(id):
    time.sleep(600)
    User.query.filter_by(id=id).update({'vcode':None})
    db.session.commit()

# Sets user verification code to a random 7 digit string 
def set_verification_code():
    code = randrange(1000000, 9999999)
    user = get_user()
    user.vcode = code
    db.session.commit()
    thread = threading.Thread(target=verification_timeout, args=[user.id])
    thread.start()
    return code

# Send email to the current user with verification code
def send_verification_code(app):
    verifcation_code = set_verification_code()
    user = get_user()
    msg = Message(
        'My App Verification', 
        sender=vcode_sender,
        recipients = [user.email])
    msg.html = render_template(
        'email/verification.html', 
        verifcation_code=verifcation_code, 
        v_url=f"{base_url}/email-verification")
    return send_email(app, msg, 'email-verification')


def valid_domain(email):
    domain = email[email.index('@') + 1:]
    if limit_domains == False:
        return True
    elif domain in domains:
        return True
    else:
        return False

def is_authenticated():
    user = get_user()
    if current_user.is_authenticated \
    and user.is_verified:
        return True
    else:
        return False
