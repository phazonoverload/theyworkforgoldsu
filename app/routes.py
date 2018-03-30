from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user
from app import app
from app.forms import LoginForm
from app.models import User

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
    # If already logged in, chuck them back to home
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    # If request comes with form data
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        # failed login
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username of password')
            return redirect(url_for('login'))
        # Login the user and push back to home
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    # If request does not come with form data
    return render_template("login.html", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))