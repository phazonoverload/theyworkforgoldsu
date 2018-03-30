from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

class LoginForm(FlaskForm):
  email = StringField('Email Address', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  remember_me = BooleanField('Remember Me')
  submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
  username = StringField('Full Name', validators=[DataRequired()])
  email = StringField('Email Address', validators=[DataRequired(), Email()])

  role = SelectField('Role Title', choices=[("president", "President"), ("education", "Education Officer"), ("campaigns-activities", "Campaigns & Activities Officer"), ("welfare-diversity", "Welfare & Diversity Officer"), ("wired", "Wired Radio Station Managers"), ("housing", "Housing Officer"), ("sports", "Sports Officer"), ("bme", "Black and Minority Ethnic Students' Officer"), ("womens", "Women's Officer"), ("trans-nb", "Trans and Non-Binary Students' Officer"), ("campaigns", "Campaigns Officer"), ("leopard", "Leopard Editor"), ("trustees", "Student Trustees")], validators=[DataRequired()])

  role_type = SelectField('Select Type', choices=[("ft", "Full Time Sabbatical"),("pt", "Part Time"), ("media", "Media Manager")], validators=[DataRequired()])

  password = PasswordField('Password', validators=[DataRequired()])
  password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
  passphrase = StringField('Passphrase', validators=[DataRequired()])
  submit = SubmitField('Register')

  def validate_passphrase(self, passphrase):
    if passphrase.data != "Druid!":
      raise ValidationError("Passphrase is not correct")
