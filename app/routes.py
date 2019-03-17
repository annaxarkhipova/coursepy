

from flask import render_template, flash, redirect, url_for, send_from_directory
from . import app
from app.forms import LoginForm
from flask_login import current_user, login_user
from app.models import User
from flask_login import logout_user


@app.route('/')
@app.route('/index')
def index():
    user = {'username': ' Anna'}
    posts = [
        {
            'author': {'username': 'Roman'},
            'body': 'Hi yall!'
        },
        {
            'author': {'username': 'Jaykob'},
            'body': 'Are you alright?'
        },
        {
            'author': {'username': 'Tim'},
            'body': 'Definitely'
        }
    ]
    return render_template('index.html', title='Home',  posts=posts) #user=user,

# GET-запросы — возвращают информацию клиенту (браузер), POST - передают инфо серверу
@app.route('/login', methods=['GET', 'POST'])# cообщаем Flask о необходимости принимать запросы
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
