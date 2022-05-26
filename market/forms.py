from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,EmailField,PasswordField


class RegisterForm(FlaskForm):
    username=StringField(label='Username:')
    email_address=EmailField(label='Email Address:')
    password1=PasswordField(label='Password:')
    password2=PasswordField(label='Confirm Password:')
    submit=SubmitField(label='Create Account:')