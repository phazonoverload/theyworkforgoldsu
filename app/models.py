from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login

class Role(db.Model):
  __tablename__ = 'role'
  value = db.Column(db.String(128), index=True, unique=True, primary_key=True)
  label = db.Column(db.String(128), unique=True)
  role_type = db.Column(db.String(128), unique=True)

  def __repr__(self):
    return '[Role {}]'.format(self.label)

class User(UserMixin, db.Model):
  __tablename__ = 'user'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(128), index=True, unique=True)
  email = db.Column(db.String(128), index=True, unique=True)
  role = db.Column(db.String(64), index=True, unique=True)
  twitter = db.Column(db.String(64))
  resigned = db.Column(db.Boolean(), index=True, default=False)
  password_hash = db.Column(db.String(128))
  signed_up = db.Column(db.DateTime, default=datetime.utcnow)
  promises = db.relationship("Promise")
  updates = db.relationship("Update")

  def __repr__(self):
    return '[User {}]'.format(self.name)

  def set_password(self, password):
    self.password_hash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
  return User.query.get(int(id))

class Promise(db.Model):
  __tablename__ = 'promise'
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer())
  body = db.Column(db.String(128))
  actionable = db.Column(db.Boolean(), index=True)
  state = db.Column(db.Integer())
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

  def __repr__(self):
    return '[Promise {}]'.format(self.body)

class Update(db.Model):
  __tablename__ = 'update'
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer())
  month = db.Column(db.String(128))
  datetime = db.Column(db.DateTime, default=datetime.utcnow)
  general = db.Column(db.String(1000))
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

  def __repr__(self):
    return '[Update {}]'.format(self.general)