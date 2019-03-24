

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    text = TextAreaField('Text', validators=[DataRequired()])
    send = SubmitField('Send')

class LoginForm(FlaskForm):
    username = StringField('Title', validators=[DataRequired()])
    password = TextAreaField('Text', validators=[DataRequired()])
    login = SubmitField('Log In')

class CommentForm(FlaskForm):
    text = TextAreaField('Text', validators=[DataRequired()])
    send = SubmitField('Send')
