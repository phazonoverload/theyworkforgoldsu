from flask import render_template
from app import app
from app.forms import LoginForm

users = [
    {
        "name": "Joe Leam",
        "role": "Campaigns & Activities Officer",
        "type": "full",
        "page": "campaigns-activities",
        "term": 1
    },
    {
        "name": "JT Tema",
        "role": "President",
        "type": "full",
        "page": "president",
        "term": 2
    }
]

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', users=users)

@app.route('/officer')
def officers():
    user = users[0]
    return render_template('officer.html', user=user)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", form=form)