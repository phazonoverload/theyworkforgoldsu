from flask import Flask, request, render_template, redirect, url_for
import pymysql

class DBHelper:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='kevin', passwd='123', db='twits')
    def get_all_twits(self):
      query = "select u.username, t.twit_id, t.twit, t.created_at from twits t, users u where t.user_id=u.user_id order by t.created_at desc;"
      with self.db.cursor() as cursor:
        cursor.execute(query)
        return cursor.fetchall()

app = Flask(__name__)
db = DBHelper()

@app.route('/')
def show_all():
    twits = db.get_all_twits()
    return render_template("display-all-sql.html", twits=twits)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)
