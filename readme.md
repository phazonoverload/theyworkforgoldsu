# The Work For GoldSU

Born from a desire to better understand how promises are carried through, They Work For GoldSU is a platform for elected officials at Goldsmiths Students' Union to keep a meaningful log of their progress throughout the year.

The platform will be prepopulated with the manifesto promises of the 2017-2018 full-time and part-time officers, and give them the opportunity to log progress of each promise along with a completion percentage as they see it (with anything less than 100% meaning they did not manage to complete the task).

This project is inspired by [MySociety's](https://www.mysociety.org) [TheyWorkForYou](https://www.theyworkforyou.com/) project, which aims to keep elected MPs accountable. It is built as coursework for IS52027C: Data, Networks and the Web (2017-18), and born from cynicism as a member of the Students' Union.

## License: (CC) BY-SA 4.0

This work is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

## Setting up project

Before you start, make sure you have Python and pip installed, along with [virtualenv](https://virtualenv.pypa.io/en/stable/installation/).

The first step is to `git clone` this repository. Once you've done that navigate to the newly-downloaded folder in your terminal and run the following commands:

```
# Setup a new virtual environment and install dependencies
$ virtualenv venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt

# Set up database
$ flask db upgrade
```

## Running project

```
# Enable virtualenv if you killed your terminal instance since the last time you ran this command
$ source venv/bin/activate

# Expose the entry point of our Flask app and run it
$ export FLASK_APP=main.py
$ flask run
```

## Roadmap (todo)

* Responsive views
* Dockerise
* Deploy on now.sh
* Take all instances of Goldsmiths-specific language and move to variables
* About page
* API Docs
* Home page copy

## Technical requirements for coursework

Criteria                   | Demonstrated
---------------------------|---------------------------
It is a flask app | It runs
More than one route and view | `/app/routes.py`
Uses Jinja templates | `/app/templates/*.html`
Jinja control structures | `/app/templates/officer.html`
One or more forms | `/app/templates/register.html`
Forms have validation | `/app/forms.py` both built-in and custom (`validate_passphrase()`)
Useful feedback messages | `/app/forms.py` in `validate_passphrase()`
Bonus: wtforms | `/app/forms.py` include at top, use of field types in file
Database backend with CRUD | Yes, uses sqlite. Examples below are from `/app/routes.py`<br> Create: `/promises/<id>/update`<br> Read: `/`<br>Update: `/edit`<br>Delete: Via direct database connection (purposeful)
Create & update via forms | `/app/forms.py`<br>Create: `RegistrationForm()`<br>Update: `EditUserForm()`
Bonus: SQLAlchemy | `/app/__init__.py`
User auth | /login, /register, /logout
Sessions for user | Use of `login_user()` in `/app/routes.py`
Passwords as hashes | `set_password()` and `check_password()` functions in `User` model
A way to logout | /logout
Bonus: Salts | werkzeug.security's `generate_password_hash()` and `check_password_hash()` functions salt hashes by default
Bonus: flask-login usage | Use of `current_user`, `login_user`, `logout_user` and `login_required`
Basic API | TBC: docs at /api
Bonus: GET, POST, PUSH and DELETE via API | Not suitable for this project
Bonus: flask-restful | flask-restless was sufficient