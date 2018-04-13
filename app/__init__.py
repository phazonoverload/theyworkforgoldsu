from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_gravatar import Gravatar

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
gravatar = Gravatar(app,size=400,rating='g',default='retro',force_default=False,use_ssl=True,base_url=None)
login = LoginManager(app)
login.login_view = "login"

from app import routes, models, apis