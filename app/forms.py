from app import db
from app.models import Role, User
from flask import current_app
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from wtforms_sqlalchemy.fields import QuerySelectField

########

class LoginForm(FlaskForm):
  email = StringField('Email Address', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  remember_me = BooleanField('Remember Me')
  submit = SubmitField('Sign In')

########

class RegistrationForm(FlaskForm):
  name = StringField('Full Name', validators=[DataRequired()])
  email = StringField('Email Address', validators=[DataRequired(), Email()])
  twitter = StringField('Twitter username (no @)')
  role = QuerySelectField(query_factory=lambda: Role.query, allow_blank=True, get_label='label')
  password = PasswordField('Password', validators=[DataRequired()])
  password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
  passphrase = StringField('Passphrase', validators=[DataRequired()])
  submit = SubmitField('Register')

  def validate_passphrase(self, passphrase):
    if passphrase.data != current_app.config['PASSPHRASE']:
      raise ValidationError("Passphrase is not correct")

########

class NewPromiseForm(FlaskForm):
  title = StringField('Title', validators=[DataRequired()])
  body = TextAreaField('Description', validators=[DataRequired()])
  actionable = BooleanField('Is this actionable?', validators=[DataRequired()])
  user_id = QuerySelectField(query_factory=lambda: User.query, allow_blank=True, get_label='name')
  passphrase = StringField('Passphrase', validators=[DataRequired()])
  submit = SubmitField('Submit')

  def validate_passphrase(self, passphrase):
    if passphrase.data != current_app.config['ADMIN_PASS']:
      raise ValidationError("Passphrase is not correct")

########

class NewUpdateForm(FlaskForm):
  body = TextAreaField('Update Text', validators=[DataRequired()])
  submit = SubmitField('Submit')

########