from datetime import datetime
from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from app import app, db
from app.forms import LoginForm, RegistrationForm, NewPromiseForm, NewUpdateForm, NewRoleForm, EditUserForm, EditPasswordForm
from app.models import User, Role, Update, Promise

@app.route('/')
def index():
    users = User.query.filter(User.role.has(role_type='ft'))
    pt_count = User.query.filter(~User.role.has(role_type='ft')).count()
    return render_template('index.html', users=users, pt_count=pt_count)

@app.route('/people')
def people():
    users = User.query.order_by('name').all()
    ft_count = User.query.filter(User.role.has(role_type='ft')).count()
    pt_count = User.query.filter(~User.role.has(role_type='ft')).count()
    return render_template('officers.html', users=users, ft_count=ft_count, pt_count=pt_count)

@app.route('/people/<role>')
def officer(role):
    user = User.query.filter_by(role_id=role).first_or_404()
    return render_template('officer.html', user=user, single=True, )

@app.route('/people/<role>/updates', methods=['GET', 'POST'])
def officer_updates(role):
    user = User.query.filter_by(role_id=role).first_or_404()
    updates = Update.query.filter_by(user_id=user.id).all()
    return render_template('officer_updates.html', user=user, updates=updates)

@app.route('/promises')
def promises():
    return render_template('promises.html')

@app.route('/promises/<id>')
def single_promise(id):
    promise = Promise.query.filter_by(id=id).first_or_404()
    return render_template('promise_single.html', promise=promise)

@app.route('/promises/<id>/update', methods=['GET', 'POST'])
@login_required
def update_promise(id):
    promise = Promise.query.filter_by(id=id).first_or_404()
    form = NewUpdateForm()
    if form.validate_on_submit():
        update = Update(body=str(form.body.data), user_id=current_user.id, promise_id=promise.id)
        db.session.add(update)
        db.session.commit()
        flash("New update submitted!")
        return redirect(url_for('officer', role=current_user.role_id))
    return render_template("update_single.html", promise=promise, form=form)

@app.route('/updates')
def updates():
    updates = Update.query.order_by(Update.datetime.desc()).all()
    return render_template('updates.html', updates=updates)

@app.route('/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditUserForm()
    if form.validate_on_submit():
        current_user.name = str(form.name.data)
        current_user.email = str(form.email.data)
        current_user.twitter = str(form.twitter.data)
        current_user.facebook = str(form.facebook.data)
        db.session.commit()
        flash('Changes to account made!')
    return render_template('edit.html', form=form)

@app.route('/edit/password', methods=['GET', 'POST'])
@login_required
def edit_password():
    form = EditPasswordForm()
    if form.validate_on_submit():
        if current_user.check_password(form.old_password.data):
            current_user.set_password(form.new_password.data)
            db.session.commit()
            flash('Password changed')
    return render_template('edit_password.html', form=form)

@app.route('/api')
def api_docs():
    return render_template('api.html')

@app.route('/about')
def about():
    return render_template('about.html')

###
### AUTH ROUTES
###

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(name=str(form.name.data), email=str(form.email.data), role=form.role.data, twitter=str(form.twitter.data), facebook=str(form.facebook.data))
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
        promise = Promise(title=str(form.title.data), body=str(form.body.data), user_id=form.user_id.data.id)
        db.session.add(promise)
        db.session.commit()
        flash("New Promise added")
    return render_template('admin_promise.html', form=form)

@app.route('/admin/roles', methods=['GET', 'POST'])
def admin_role():
    form = NewRoleForm()
    if form.validate_on_submit():
        role = Role(label=str(form.label.data), value=str(form.value.data), role_type=str(form.role_type.data))
        db.session.add(role)
        db.session.commit()
        flash("New Role added")
    return render_template('admin_role.html', form=form)

###
### REDIRECT ROUTES
###

@app.route('/people')
def redirect_o(role):
    return redirect(url_for('index'))