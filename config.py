import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ['SECRET_KEY'] or os.urandom(24)
    SQLALCHEMY_DATABASE_URI = os.environ['DATABSE_URL'] or \
    'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PASSPHRASE = os.environ['PASSPHRASE']
    ADMIN_PASS = os.environ['ADMIN_PASS']
