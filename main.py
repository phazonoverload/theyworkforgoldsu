from app import app, db
from app.models import User, Promise, Update, Role

@app.shell_context_processor
def make_shell_context():
  return {'db': db, 'User': User, 'Promise': Promise, 'Update': Update, 'Role': Role}