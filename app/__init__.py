import os
from pathlib import Path

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail

PROJECT_DIR = Path(__file__).absolute().parent.parent

class Config():
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(PROJECT_DIR, 'app.db') + '?check_same_thread=False'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'never-guess'


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

app.config['MAIL_SERVER']='smtp.yandex.ru'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'arkhipova-1997'
app.config['MAIL_PASSWORD'] = 'anaueva100'
app.config['MAIL_DEFAULT_SENDER'] = 'arkhipova-1997@yandex.ru'
app.config['MAIL_DEBUG'] = True
app.config['MAIL_SUPPRESS_SEND'] = True
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_MAX_EMAILS'] = 10
mail = Mail(app)



from . import routes, models