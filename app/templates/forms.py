

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField, BooleanField
from wtforms.validators import DataRequired

from app.models import Comment, User, Post

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    text = TextAreaField('Text', validators=[DataRequired()])
    send = SubmitField('Send')


class MessageForm(FlaskForm):
    text = TextAreaField('Text', validators=[DataRequired()])
    send = SubmitField('Send')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')
    remember_me = BooleanField('Remember me', default=False)

class CommentForm(FlaskForm):
    text = TextAreaField('Please leave your comment here', validators=[DataRequired()])
    send = SubmitField('Send')
