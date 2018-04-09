from flask import Flask, request, render_template, redirect, url_for
import pymongo

class DBHelper:
    def __init__(self):
        client = pymongo.MongoClient()
        self.db = client['twits']
    def get_all_twits(self):
        return self.db.twits.find().sort('created_at',pymongo.ASCENDING)

app = Flask(__name__)
db = DBHelper()

@app.route('/')
def show_all():
    twits = db.get_all_twits()
    return render_template("display-all-mongo.html", twits=twits)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)
