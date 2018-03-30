from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(128), index=True, unique=True)
  email = db.Column(db.String(128), index=True, unique=True)
  role = db.Column(db.String(64), index=True, unique=True)
  resigned = db.Column(db.Boolean(), index=True)
  password_hash = db.Column(db.String(128))

  promises = db.relationship('Promise', backref='officer', lazy='dynamic')

  def __repr__(self):
    return '<User {}>'.format(self.username)

  def set_password(self, password):
    self.password_hash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password_hash, password)

class Promise(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
  body = db.Column(db.String(128))
  actionable = db.Column(db.Boolean(), index=True)
  state = db.Column(db.Integer())

  def __repr__(self):
    return '<Post {}>'.format(self.body)