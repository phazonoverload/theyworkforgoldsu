from flask import Flask, request, render_template, redirect, url_for
import pymongo
import datetime
import os
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import ValidationError, DataRequired

class DBHelper:
  def __init__(self):
    client = pymongo.MongoClient()
    self.db = client['twits']
  def get_all(self):
    return self.db.twits.find().sort('created_at',pymongo.ASCENDING)
  def add(self, text):
    return self.db.twits.insert({'twit': text, 'username':'dan1', 'created_at': datetime.datetime.utcnow()})

app = Flask(__name__)
app.secret_key = os.urandom(24)
db = DBHelper()

class newTwitForm(FlaskForm):
  text = StringField('Text', validators=[DataRequired()])
  submit = SubmitField('Post')

@app.route('/')
def show_all():
  twits = db.get_all()
  return render_template("display-all-mongo.html", twits=twits)

@app.route("/add", methods=['GET', 'POST'])
def new_twit():
  form = newTwitForm()
  if form.validate_on_submit():
    twit = form.text.data
    db.add(twit)
    return redirect(url_for('show_all'))
  return render_template('new-shared-wtf.html', form=form)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)
