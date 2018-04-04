from app import app, db
from app.models import User, Role, Update, Promise
import flask_restless

manager = flask_restless.APIManager(app, flask_sqlalchemy_db=db)

manager.create_api(User, methods=['GET'], include_columns=['id', 'name', 'email', 'resigned', 'role', 'promises', 'updates', 'updates.id', 'updates.datetime', 'updates.body', 'updates.promise_id'], url_prefix='/api/v1', collection_name='people', primary_key='id')

manager.create_api(Update, methods=['GET'], include_columns=['id', 'datetime', 'body', 'user_id', 'promise_id'], url_prefix='/api/v1', collection_name='updates')

manager.create_api(Promise, methods=['GET'], include_columns=['id', 'title', 'body', 'actionable', 'user_id', 'updates'], url_prefix='/api/v1', collection_name='promises')
