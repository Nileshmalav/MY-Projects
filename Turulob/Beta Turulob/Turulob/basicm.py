
from datetime import datetime
from flask import Flask, render_template, request, redirect, Response, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import  ForeignKey

from datetime import datetime
from werkzeug.utils import redirect, secure_filename
from flask_login import LoginManager, UserMixin, login_user, current_user, login_required, logout_user
from flask_socketio import SocketIO, send, emit
from random import shuffle
from random import randint
import json
from authlib.integrations.flask_client import OAuth
from flask_mail import Mail
from sqlalchemy.orm import relationship

from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin ,AdminIndexView




app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'super secret key'


# mail server
# mail server

with open('config.json', 'r') as c:
    params = json.load(c)["params"]

app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    
    # MAIL_USE_TLS = True,
    # MAIL_PORT = 587,
    MAIL_USERNAME=params['gmail-user'],
    MAIL_PASSWORD=params['gmail-password']
)
mail = Mail(app)
# mail server
# mail server

db = SQLAlchemy(app)
socketio = SocketIO(app)
# configure flask

login = LoginManager(app)
login.init_app(app)
