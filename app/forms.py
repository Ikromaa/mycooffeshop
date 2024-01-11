from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, TimeField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, Regexp

# Form for user registration
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

# Form for user login
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

# Form for reservation booking
class ReservationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    nomor = StringField('Nomor Whatsapp', validators=[DataRequired(), Regexp(r'^\+?[0-9]+$', message="Format nomor tidak valid")])
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    time = TimeField('Time', format='%H:%M', validators=[DataRequired()])
    submit = SubmitField('Book')
