


from werkzeug.security import generate_password_hash, check_password_hash
from app import login
from app import db
from datetime import datetime
from flask_login import UserMixin
from hashlib import md5


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.Column(db.Text)

    # followers = db.Table('followers', db.Column('follower_id', db.Integer, db.ForeignKey('user.id')), db.Column('followed_id', db.Integer, db.ForeignKey('user.id')))
    #
    # followed = db.relationship('User', secondary=followers,
    #                            primaryjoin=(followers.follower_id == id),
    #                            secondaryjoin=followers.__table__,
    #                            backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')


    # def follow(self, user):
    #     if not self.is_following(user):
    #         self.followed.append(user)
    #
    # def unfollow(self, user):
    #     if self.is_following(user):
    #         self.followed.remove(user)
    #
    # def is_following(self, user):
    #     return self.followed.filter(self.followers.c.followed_id == user.id).count() > 0

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://pp.userapi.com/c845019/v845019144/1c861c/3XeARpgPEGo.jpg'.format(
            digest, size)

    def __repr__(self):
        return '<User {}>'.format(self.username)



class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(300))
    created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    message_id = db.Column(db.Integer, db.ForeignKey('message.id'))

    def __repr__(self):
        return '<Message {}>'.format(self.body)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    username = db.Column(db.String(64), index=True, unique=True)

    # someone_likes_it = db.Column('like', db.Integer, db.ForeignKey('user.id'))
    # post_liked_by = db.Column('likedby1', db.Integer, db.ForeignKey('user.id'))



    def __repr__(self):
        return '<Post {}>'.format(self.body)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    username = db.Column(db.String(64), index=True, unique=True)

    def __repr__(self):
        return '<Comment {}>'.format(self.body)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))