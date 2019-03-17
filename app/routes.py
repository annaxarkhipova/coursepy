
from . import app
from flask import render_template, flash, redirect, url_for, send_from_directory
from app.forms import LoginForm
from flask_login import logout_user, current_user, login_user, login_required
from app.models import User


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Hello everyone!'},
        {'author': user, 'body': 'Today was good'}
    ]
    return render_template('user.html', user=user, posts=posts)

@app.route('/')
@app.route('/index')
def index():
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
    return render_template('index.html', title='Home',  posts=posts)

# GET-запросы — возвращают информацию клиенту (браузер), POST - передают инфо серверу
@app.route('/login', methods=['GET', 'POST'])
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

