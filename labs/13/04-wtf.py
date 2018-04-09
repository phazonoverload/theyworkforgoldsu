from flask import Flask, render_template
from flask import request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
USERNAME = 'kev'
PASSWORD = 'Pass!'

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        if username == USERNAME and password == PASSWORD:
            flash('login successful!')
        else:
            flash('Bad creds')
    return render_template('wtf.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
