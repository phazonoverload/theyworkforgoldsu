from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login

class Roles(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(128), unique=True)
  slug = db.Column(db.String(128), index=True, unique=True)

  def __repr__(self):
    return '<ROles {}>'.format(self.title)

class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(128), index=True, unique=True)
  email = db.Column(db.String(128), index=True, unique=True)
  role = db.Column(db.String(64), index=True, unique=True)
  role_type = db.Column(db.String(64))
  twitter = db.Column(db.String(64))
  resigned = db.Column(db.Boolean(), index=True, default=False)
  password_hash = db.Column(db.String(128))
  last_seen = db.Column(db.DateTime, default=datetime.utcnow)

  promises = db.relationship('Promise', backref='officer', lazy='dynamic')

  def __repr__(self):
    return '<User {}>'.format(self.username)

  def set_password(self, password):
    self.password_hash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
  return User.query.get(int(id))

class Promise(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer())
  body = db.Column(db.String(128))
  actionable = db.Column(db.Boolean(), index=True)
  state = db.Column(db.Integer())

  updates = db.relationship('Update', backref='promise', lazy='dynamic')

  def __repr__(self):
    return '<Post {}>'.format(self.body)

class Update(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer())
  month = db.Column(db.String(128))
  datetime = db.Column(db.DateTime, default=datetime.utcnow)
  general = db.Column(db.String(1000))

  def __repr__(self):
    return '<Post {}>'.format(self.general)