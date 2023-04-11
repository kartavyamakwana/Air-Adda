from flask import get_flashed_messages, render_template,url_for,flash,redirect
from airline.forms import RegistrationForm, LoginForm 
from airline.models import User,Flight
from airline import app, db, bcrypt
from flask_login import login_user,current_user,logout_user

@app.route('/')
@app.route('/home')
def home():
    messages = get_flashed_messages(with_categories=True)
    return render_template('index.html',messages=messages)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password','danger')
    return render_template('login.html',title='Login',form=form,styles=['static/login_style.css'])

@app.route('/signup',methods=['GET','POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created!','success')
        return redirect(url_for('login'))
    return render_template('signup.html',title='SignUp',form=form,styles=['static/signup_style.css'])

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))
