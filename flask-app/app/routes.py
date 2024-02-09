"""Routes for parent Flask app."""
from flask import render_template, request, url_for, flash, redirect, request
from app.lib.forms import RegistrationForm, LoginForm, EmailVerificationForm
from app.models import User
from app import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
from os import environ
from time import strftime
import traceback
import json
from werkzeug.exceptions import HTTPException
from .lib.logging import *
from . import app
from .lib import auth

base_url = environ.get("BASE_URL")

# ----------------------------------- Views ---------------------------------- #

# Homepage
@app.route("/")
def home():
    """Landing page."""
    return render_template(
        "index.html",
        title="Tide Pool Apps",
        description="Dash Flask App",
        template="home-template",
        body="This is a homepage served with Flask.",
        login_url=url_for('login')
    )

# Login
@app.route("/login", methods=['GET', 'POST'])
def login():
    # Redirdect to homepage if the user is already logged in and verified
    if current_user.is_authenticated and current_user.is_verified:
        return redirect('/') 
    # Redirect to email verification if user email isn't verified
    elif current_user.is_authenticated and current_user.is_verified == False:
        return redirect('/email-verification')
    
    form = LoginForm()
    try:
        # Email and password validation
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                # Redirect to homepage after login if user is verified
                if user.verified == True:
                    return redirect("/")
                # Redirect to email verification after login if user isn't verified
                else:
                    return redirect("/email-verification")
            # Show error message if validation fails
            else:
                flash('Invalid email or password', 'danger')
    # Show error message if there's a login error
    except Exception as e:
        flash(e, "danger")
    return render_template(
        'login.html', title='Login',
        form=form,
        template="login-template",
    )

# Registration
@app.route("/register", methods=['GET', 'POST'])
def register():
    # Redirect to homepage if user is logged in
    if auth.is_authenticated():
        return redirect(url_for('home'))
    if current_user.is_authenticated and current_user.is_verified == False:
        return redirect("/email-verification")
    form = RegistrationForm()
    # Validate registration form
    try:
        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(
                form.password.data).decode('utf-8')
            user = User(fname=form.fname.data, lname=form.lname.data,
                        organization=form.organization.data, email=form.email.data, password=hashed_password)
            db.session.add(user)
            db.session.commit()
            # Redirect to login page if validation is successful
            return redirect(url_for('login'))
    # Display error message if registration fails
    except Exception as e:
        flash(e, "danger")
        
    return render_template(
        'register.html',
        title='Register',
        form=form,
        template="register-template",
    )

# Email Verification
@app.route("/email-verification", methods=['GET', 'POST'])
def verify():
    if current_user.is_authenticated and current_user.is_verified == False:
        # If user verification code hasn't been sent, redirect to send verification
        if current_user.vcode == None:
            return redirect("/send-verification")
        # Show verification form
        else:
            form = EmailVerificationForm()
            def template(err):
                return render_template(
                    'verification.html',
                    title='Email Verification',
                    form=form,
                    template='verification-template',
                    error_message=err
                )
            # Verify user upon form validation and matching verification codes
            if form.validate_on_submit():
                if form.verification_code.data == current_user.vcode and current_user.vcode:
                    current_user.verified = True
                    db.session.commit()
                    return redirect('/')
                else:
                    err = 'Verification code is not valid. Try again.'
                    return template(err)
            return template(None)
    # Redirect to login page if user isn't logged in
    elif current_user.is_authenticated == False:
        return redirect(url_for('login'))
    # Redirect to homepage if user isn't logged in
    else:
        redirect('/')
        
# Logout user    
@app.route("/logout")
def logout():
    logout_user()
    return redirect(base_url)

# Send email verification code
@app.route("/send-verification")
def index():
    if current_user.is_authenticated:
        return auth.send_verification_code(app)
    else:
        redirect(url_for('login'))


# ------------------------------ Error Handling ------------------------------ #

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template(
        "error/404.html",
        error=e
    ), 404

# Internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template(
        "error/500.html",
        error=e
    ), 500

# Error Logging
@app.errorhandler(HTTPException)
def handle_exception(e):
    # log error
    tb = traceback.format_exc()
    timestamp = strftime('[%Y-%b-%d %H:%M]')
    error_logger.error(
        f"""{timestamp} {request.remote_addr} {request.method} {request.scheme} {request.full_path} {e.code} ERROR\n "{e.name}: {e.description}"\n{tb}""")

    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response
