from flask_wtf import FlaskForm
from wtforms  import StringField, SubmitField, PasswordField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from app.models import User
from app.lib.auth import valid_domain

class LoginForm(FlaskForm):
	email = StringField('User', validators = [DataRequired()])
	password = PasswordField('Password', validators = [DataRequired()])
	submit = SubmitField('Login')

class RegistrationForm(FlaskForm):

    fname = StringField('First Name',
                        validators=[DataRequired(), Length(min=1, max=64)])
    lname = StringField('Last Name',
                        validators=[DataRequired(), Length(min=1, max=64)])
    organization = StringField('Organization',
                        validators=[DataRequired(), Length(min=2, max=64)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=2, max=512)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')
    
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first() 
        if user:
            raise ValidationError("There's already an account associated with this email address.")
        if valid_domain(email.data) == False:
            raise ValidationError("Your organization is not currently supported.")

class EmailVerificationForm(FlaskForm):
	verification_code = StringField('Verification Code', validators=[
	                                DataRequired(), Length(min=7, max=7)])
	submit = SubmitField('Submit')