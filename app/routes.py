

from . import app
from flask import render_template, flash, redirect, url_for
from app.templates.forms import PostForm, CommentForm, LoginForm
from flask_login import logout_user, current_user, login_user, login_required
from app.models import User, Post, Comment
from app import db
from flask import request
from werkzeug.urls import url_parse


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Hello everyone!'} ]
    return render_template('user.html', user=user, posts=posts)


@app.route('/posts/{post_id}')
def post(post_id):
    post = Post.query.get(post_id)
    return render_template('post.html', post=post)


@app.route('/create', methods=['GET', 'POST'])
def create():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, body=form.text.data)
        db.session.add(post)
        db.session.commit()
        flash('Post published!')
        return redirect('//user/<username>')
    return render_template('create_post.html', title='New Post', form=form)

    # com = CommentForm()
    # if com.validate_on_submit():
    #     com = Comment(body=c.text.data)
    #     flash('Comment posted')
    #     return redirect('/posts/{post_id}')


@app.route('/')
@app.route('/index')
def index():
    form = PostForm()
    posts = Post.query.filter_by(body=form.text.data).first()
    return render_template('index.html', title='Home', posts=posts)




# GET-запросы — возвращают инфo клиенту (браузер), POST - передают инфо серверу
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
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/follow/<username>')
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User {} not found.'.format(username))
        return redirect(url_for('index'))
    if user == current_user:
        flash('You cannot follow yourself!')
        return redirect(url_for('user', username=username))
    current_user.follow(user)
    db.session.commit()
    flash('You are following {}!'.format(username))
    return redirect(url_for('user', username=username))

@app.route('/unfollow/<username>')
@login_required
def unfollow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User {} not found.'.format(username))
        return redirect(url_for('index'))
    if user == current_user:
        flash('You cannot unfollow yourself!')
        return redirect(url_for('user', username=username))
    current_user.unfollow(user)
    db.session.commit()
    flash('You are not following {}.'.format(username))
    return redirect(url_for('user', username=username))