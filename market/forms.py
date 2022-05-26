from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField
from wtforms.validators import Length, Email, DataRequired, EqualTo


class RegisterForm(FlaskForm):
    username = StringField(label='Username:', validators=[
                           Length(min=2, max=30), DataRequired()])
    email_address = EmailField(label='Email Address:', validators=[
                               Email(), DataRequired()])
    password1 = PasswordField(label='Password:',validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(
        label='Confirm Password:', validators=[EqualTo(password1)])
    submit = SubmitField(label='Create Account')
