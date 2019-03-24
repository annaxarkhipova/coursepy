


import os
from pathlib import Path

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

PROJECT_DIR = Path(__file__).absolute().parent.parent

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(PROJECT_DIR, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'never-guess'


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

from . import routes, models