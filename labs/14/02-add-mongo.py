from flask import Flask, request, render_template, redirect, url_for
import pymongo
import datetime

class DBHelper:
  def __init__(self):
    client = pymongo.MongoClient()
    self.db = client['twits']
  def get_all(self):
    return self.db.twits.find().sort('created_at',pymongo.ASCENDING)
  def add(self, text):
    return self.db.twits.insert({'twit': text, 'username':'dan1', 'created_at': datetime.datetime.utcnow()})

app = Flask(__name__)
db = DBHelper()

@app.route('/')
def show_all():
  twits = db.get_all()
  return render_template("display-all-mongo.html", twits=twits)

@app.route("/add", methods=['GET', 'POST'])
def new_twit():
  if request.form.get('text'):
    twit = request.form['text']
    db.add(twit)
    return render_template('display-all-mongo.html')
  return render_template('new.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)
