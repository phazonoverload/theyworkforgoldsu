from flask import render_template, flash, redirect
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

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect('/')
    return render_template("login.html", form=form)