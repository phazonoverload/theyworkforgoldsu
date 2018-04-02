from datetime import datetime
from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from app import app, db
from app.forms import LoginForm, RegistrationForm, NewPromiseForm, NewUpdateForm
from app.models import User, Role, Update, Promise

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/people/<role>')
def officer(role):
    user = User.query.filter_by(role_id=role).first_or_404()
    # Show all promises from this user in this view
    return render_template('officer.html', user=user)

@app.route('/people/<role>/updates', methods=['GET', 'POST'])
def officer_updates(role):
    user = User.query.filter_by(role_id=role).first_or_404()
    # Show all updates from this user in this view
    return render_template('index.html', user=user)

@app.route('/promises')
def promises():
    # Show all promises
    return render_template('index.html')

@app.route('/promises/<id>')
def single_promise(id):
    # Show single promise and all updates related to it
    return render_template('index.html')

@app.route('/promises/<id>/update', methods=['GET', 'POST'])
@app.route('/promises/<id>/update/', methods=['GET', 'POST'])
@login_required
def update_promise(id):
    promise = Promise.query.filter_by(id=id).first_or_404()
    form = NewUpdateForm()
    if form.validate_on_submit():
        update = Update(body=str(form.body.data), user_id=current_user.id, promise_id=promise.id)
        db.session.add(update)
        db.session.commit()
        flash("New update submitted!")
        return render_template('officer.html', user=current_user)
    return render_template("update_single.html", promise=promise, form=form)

@app.route('/updates')
def updates():
    # Show all updates
    return render_template('index.html')

###
### AUTH ROUTES
###

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

@app.route('/admin/promises', methods=['GET', 'POST'])
def admin_promise():
    form = NewPromiseForm()
    if form.validate_on_submit():
        promise = Promise(body=str(form.body.data), actionable=form.actionable.data, user_id=form.user_id.data.id)
        db.session.add(promise)
        db.session.commit()
        flash("New Promise added")
    return render_template('admin_promise.html', form=form)

@app.route('/admin/people')
def admin_people_list():
    # List users and their edit links here
    return render_template('index.html')

@app.route('/admin/people/<role>', methods=['GET', 'POST'])
def admin_people_edit(role):
    # Show single user edit with passphrase
    return render_template('index.html')

###
### REDIRECT ROUTES
###

@app.route('/people')
def redirect_o(role):
    return redirect(url_for('index'))