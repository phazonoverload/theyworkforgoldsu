from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@app.route('/officer/<role>')
def officer(role):
    user = User.query.filter_by(role=role).first_or_404()
    promises = [
        {'officer': user,
        'user_id': user.id, 'body': "Promise 1 goes here", "actionable": True,
        "state": 3},
        {'officer': user,
        'user_id': user.id, 'body': "Promise 2 goes here", "actionable": False,
        "state": 5},
        {'officer': user,
        'user_id': user.id, 'body': "Promise 3 goes here", "actionable": True,
        "state": 1}
    ]
    return render_template('officer.html', user=user, promises=promises)

@app.route("/login", methods=['GET', 'POST'])
def login():
    # If already logged in, chuck them back to home
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    # If request comes with form data
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        # failed login
        if user is None or not user.check_password(form.password.data):
            flash('Invalid email address or password')
            return redirect(url_for('login'))
        # Login the user and push back to home
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('profile'))
    # If request does not come with form data
    return render_template("login.html", form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, role=form.role.data, role_type=form.role_type.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("New account registered")
        return redirect(url_for("login"))
    return render_template("register.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))