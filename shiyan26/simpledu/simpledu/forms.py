from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Length, Email, EqualTo, Required

class RegisterForm(FlaskForm):
    username = StringField('User Name:', validators=[Required(), Length(3, 24)])
    email = StringField('Email:', validators=[Required(), Email(message='Please input currect email address!')])
    password = PasswordField('Password:', validators=[Required(), Length(6, 24)])
    repeat_password = PasswordField('Repeat_password:', validators=[Required(), EqualTo('password')])
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Required(), Email(message='Please input currect email address!')])
    password = PasswordField('Password', validators=[Required(), Length(6, 24)])
    remember_me = BooleanField('Remember me!')
    submit = SubmitField('Submit')

