from flask_wtf import FlaskForm 
from wtforms import StringField,PasswordField,SubmitField,BooleanField, DateField, IntegerField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from airline.models import User

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
    
class BookingForm(FlaskForm):
    fromCity = StringField('From')
    toCity = StringField('To')
    departureDate = DateField('Departure')
    adults = IntegerField('Adults')
    children = IntegerField('Children')
