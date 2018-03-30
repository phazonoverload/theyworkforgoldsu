# The Work For GoldSU

Born from a desire to better understand how promises are carried through, They Work For GoldSU is a platform for elected officials at Goldsmiths Students' Union to keep a meaningful log of their progress throughout the year.

The platform will be prepopulated with the manifesto promises of the 2017-2018 full-time and part-time officers, and give them the opportunity to log progress of each promise along with a completion percentage as they see it (with anything less than 100% meaning they did not manage to complete the task).

This project is inspired by [MySociety's](https://www.mysociety.org) [TheyWorkForYou](https://www.theyworkforyou.com/) project, which aims to keep elected MPs accountable. It is built as coursework for IS52027C: Data, Networks and the Web (2017-18), and born from cynicism as a member of the Students' Union.


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

## Technical requirements for coursework

- [x] it is a flask app
  - [x] there is more than one route and more than one view
- [x] the html is rendered using jinja templates
  - [x] the jinja templates include some control structure(S) e.g. if/else, for/endfor
- [x] it includes one or more forms
  - [x] the forms have some validation
  - [x] there are useful feedback messages to the user
  - [x] using wtforms is not required but is recommended
- [ ] it has a database backend that implements CRUD operations
  - [ ] the database can be mysql or mongodb
  - [ ] the create & update operations take input data from a form or forms
  - [ ] using sqlalchemy is not required but will attract credit
- [x] there is user authentication (i.e. logins)
  - [x] the login process uses sessions
  - [x] passwords should be stored as hashes
  - [ ] using a salt is not required but is recommended
  - [x] there is a way to logout
  - [x] use of flask-login is not required but is recommended
- [ ] there is a basic api i.e. content can be accessed as json via http methods
  - [ ] it should be clear how to access the api (this could include comments in code)
  - [ ] additional credit will be given for an api that implements get,post,push and delete
  - [ ] use of flask-restful is not required but is recommended