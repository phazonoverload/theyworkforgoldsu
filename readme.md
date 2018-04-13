# The Work For GoldSU

Born from a desire to better understand how promises are carried through, They Work For GoldSU is a platform for elected officials at Goldsmiths Students' Union to keep a meaningful log of their progress throughout the year.

The platform will be prepopulated with the manifesto promises of the 2017-2018 full-time and part-time officers, and give them the opportunity to log progress of each promise along with a completion percentage as they see it (with anything less than 100% meaning they did not manage to complete the task).

This project is inspired by [MySociety's](https://www.mysociety.org) [TheyWorkForYou](https://www.theyworkforyou.com/) project, which aims to keep elected MPs accountable. It is built as coursework for IS52027C: Data, Networks and the Web (2017-18).

## License: (CC) BY-SA 4.0

This work is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

## Setting up project first time

Before you start, make sure you have Python and pip installed, along with [virtualenv](https://virtualenv.pypa.io/en/stable/installation/).

The first step is to `git clone` this repository. Once you've done that navigate to the newly-downloaded folder in your terminal and run the following commands:

```
# Setup a new virtual environment and install dependencies
$ virtualenv venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt


# Set up database
$ export FLASK_APP=main.py
$ flask db upgrade
```

## Running project

```
# Enable virtualenv if you killed your terminal instance since the last time you ran this command
$ source venv/bin/activate


# Set environment variable, expose the entry point of our Flask app and run it
$ export FLASK_APP=main.py
$ export FLASK_DEBUG=1
$ export PASSPHRASE=passphrase
$ export ADMIN_PASS=admin
$ flask run
```

This sets the registration passphrase to 'passphrase' and the administration passhrase to 'admin'

## Deploying project

I have hosted this projecton Heroku's Hobbiest Tier. Here is how...

1. Clone this repo and ensure you have the Heroku CLI installed
2. `heroku login`
3. `heroku apps:create YourHerokuAppName`
4. `heroku addons:add heroku-postgresql:hobby-dev`
5. `heroku config:set FLASK_APP=main.py`
6. `git push heroku master`

Go into your Heroku admin panel, head to the application you created and go to the settings tab. Reveal the config vars, and set the following vars:

* FLASK_APP to main.py
* PASSPHRASE to your registration passphrase
* ADMIN_PASS to your administration passphrase

When you want to deploy updates, create a new git commit and run the final git push command again.