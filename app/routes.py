from datetime import datetime
from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from app import app, db
from app.forms import LoginForm, RegistrationForm, NewPromiseForm
from app.models import User, Role, Update, Promise

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/o/<role>', methods=['GET', 'POST'])
def officer(role):
    user = User.query.filter_by(role_id=role).first_or_404()
    return render_template('officer.html', user=user)

@app.route('/update', methods=['GET', 'POST'])
@login_required
def update():
    promises = Promise.query.filter_by(user_id=current_user.id)
    return render_template("update.html", promises=promises)

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
        return redirect(url_for('index'))
    # If request does not come with form data
    return render_template("login.html", form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(name=str(form.name.data), email=str(form.email.data), role=form.role.data, twitter=str(form.twitter.data))
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

###
### ADMIN ROUTES
###

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/admin/promise', methods=['GET', 'POST'])
def admin_promise():
    form = NewPromiseForm()
    if form.validate_on_submit():
        promise = Promise(body=str(form.body.data), actionable=form.actionable.data, user_id=form.user_id.data.id)
        db.session.add(promise)
        db.session.commit()
        flash("New Promise added")
    return render_template('admin_promise.html', form=form)

###
### REDIRECT ROUTES
###

@app.route('/o')
def redirect_o(role):
    return redirect(url_for('index'))