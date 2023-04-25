from flask_wtf import FlaskForm 
from wtforms import StringField,PasswordField,SubmitField,BooleanField, DateField, IntegerField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError, InputRequired
from airline.models import User
from flask import flash
from datetime import datetime

class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                           validators=[DataRequired(),Length(min = 2,max=20)])
    email = StringField('Email',
                            validators=[DataRequired(),Email()])    
    password = PasswordField('Password',
                             validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign Up')
    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Choose another one')
    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email is already in use!')

class LoginForm(FlaskForm):
    email = StringField('Email',
                            validators=[DataRequired(),Email()])    
    password = PasswordField('Password',
                             validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
    
def valid_city(form, field):
    cities = ['Ahmedabad', 'Goa', 'Mumbai']
    found=0
    for city in cities:
        if city == str(field.data):
            found=1
            break
    
    if found == 0:
        flash('City not found in the database', 'danger')
        raise ValidationError('City not found in the database')

def valid_passengers(form, field):
    if field.data < 0:
        flash('Number of passengers cannot be negative')
        raise ValidationError('Cannot be negative')

def valid_date(form, field):
    now = datetime.utcnow().date()
    if field.data < now:
        flash('You have missed the flight!', 'danger')
        raise ValidationError('Flight miss')

class BookingForm(FlaskForm):
    fromCity = StringField('From', validators=[InputRequired(), valid_city])
    toCity = StringField('To', validators=[InputRequired(), valid_city])
    departureDate = DateField('Departure', validators=[InputRequired(), valid_date])
    adults = IntegerField('Adults', validators=[InputRequired(), valid_passengers], default=0)
    children = IntegerField('Children', validators=[InputRequired(), valid_passengers], default=0)
    submit = SubmitField('Search')
