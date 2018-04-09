from flask import Flask, render_template, request, flash
import string

app = Flask(__name__)
app.secret_key = "123abc"

USERNAME = "kev"
PASSWORD = "Pass!"


@app.route("/", methods=['GET', 'POST'])
def show_user():
    if request.method == 'POST':
        username = request.form['user']
        password = request.form['pass']
        if username == USERNAME and password == PASSWORD:
            flash('Logged in!')
        else:
            flash('Bad creds')
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
