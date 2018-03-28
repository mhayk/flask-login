import os
from config import login_manager, app, db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'
    id            = db.Column('id', db.Integer, primary_key=True)
    username      = db.Column('username', db.String(18), unique=True, index=True)
    password      = db.Column('password', db.String(255))
    email         = db.Column('email', db.String(60), unique=True, index=True)

    def __init__(self, username, password, email):
        self.username = username
        self.set_password(password)
        self.email = email

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<User {}>'.format(self.username)