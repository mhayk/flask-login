import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.login import login_user, logout_user, current_user, login_required
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456789'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:m2smart@localhost/flask'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@192.168.56.128/flask'
app.config['DEBUG'] = True
app.config['REMEMBER_COOKIE_DURATION'] = timedelta(minutes = 30)

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
