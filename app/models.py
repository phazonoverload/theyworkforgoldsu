from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login

class Role(db.Model):
  id = db.Column(db.Integer, unique=True, primary_key=True)
  value = db.Column(db.String(128), index=True, unique=True)
  label = db.Column(db.String(128), unique=True)
  role_type = db.Column(db.String(128))
  users = db.relationship('User', backref='role', lazy='dynamic')
  promises = db.relationship('Promise', backref='role', lazy='dynamic')

  def __repr__(self):
    return '[Role {}]'.format(self.label)

class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  role_id = db.Column(db.String(64), db.ForeignKey('role.value'), index=True)
  name = db.Column(db.String(128), index=True, unique=True)
  email = db.Column(db.String(128), index=True, unique=True)
  twitter = db.Column(db.String(64))
  facebook = db.Column(db.String(64))
  resigned = db.Column(db.Boolean(), index=True, default=False)
  password_hash = db.Column(db.String(128))
  signed_up = db.Column(db.DateTime, default=datetime.utcnow)
  updates = db.relationship('Update', backref='user', lazy='dynamic')

  def __repr__(self):
    return '[User {}]'.format(self.name)

  def set_password(self, password):
    self.password_hash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password_hash, password)

class Promise(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(128))
  body = db.Column(db.String(256))
  actionable = db.Column(db.Boolean(), index=True)
  role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
  updates = db.relationship('Update', backref='promise', lazy='dynamic')

  def __repr__(self):
    return '[Promise {}]'.format(self.title)

class Update(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  datetime = db.Column(db.DateTime, default=datetime.utcnow)
  body = db.Column(db.String(1000))
  personal = db.Column(db.String(1000))
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  promise_id = db.Column(db.Integer, db.ForeignKey('promise.id'))

  def __repr__(self):
    return '[Update {}]'.format(self.body)

@login.user_loader
def load_user(id):
  return User.query.get(int(id))