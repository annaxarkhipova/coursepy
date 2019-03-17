

from flask import render_template, flash, redirect, send_from_directory
from . import app
from app.forms import LoginForm


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
    return render_template('index.html', title='Home', user=user, posts=posts)

# GET-запросы — возвращают информацию клиенту (браузер), POST - передают инфо серверу
@app.route('/login', methods=['GET', 'POST']) # cообщаем Flask о необходимости принимать запросы
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Log in requested for user {}, remember_me={}'.format(  # flash - cбщ подтверждающее, что учетные данные были получены
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

