from flask import Flask, request, render_template, redirect, url_for
import pymysql
import os
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import ValidationError, DataRequired

class DBHelper:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='kevin', passwd='123', db='twits')
    def get_all(self):
      query = "select u.username, t.twit_id, t.twit, t.created_at from twits t, users u where t.user_id=u.user_id order by t.created_at desc;"
      with self.db.cursor() as cursor:
        cursor.execute(query)
        return cursor.fetchall()
    def add(self, text):
        q = "insert into twits (twit, user_id) values ('{}', '{}')".format(text, 1)
        with self.db.cursor() as cursor:
            cursor.execute(q)
            return self.db.commit()

app = Flask(__name__)
app.secret_key = os.urandom(24)
db = DBHelper()

class newTwitForm(FlaskForm):
  text = StringField('Text', validators=[DataRequired()])
  submit = SubmitField('Post')

@app.route('/')
def show_all():
    twits = db.get_all()
    return render_template("display-all-sql.html", twits=twits)

@app.route('/add', methods=['GET', 'POST'])
def new_twit():
  form = newTwitForm()
  if form.validate_on_submit():
    twit = form.text.data
    db.add(request.form['text'])
    return redirect(url_for('show_all'))
  return render_template('new-shared-wtf.html', form=form)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)
