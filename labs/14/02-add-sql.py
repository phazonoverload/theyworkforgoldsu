from flask import Flask, request, render_template, redirect, url_for
import pymysql

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
db = DBHelper()

@app.route('/')
def show_all():
    twits = db.get_all()
    return render_template("display-all-sql.html", twits=twits)

@app.route('/add', methods=['GET', 'POST'])
def new_twit():
    if request.form.get('text'):
        db.add(request.form['text'])
        return redirect(url_for('show_all'))
    return render_template('new-shared.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)
