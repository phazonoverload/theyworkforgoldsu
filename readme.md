# The Work For GoldSU

Born from a desire to better understand how promises are carried through, They Work For GoldSU is a platform for elected officials at Goldsmiths Students' Union to keep a meaningful log of their progress throughout the year.

The platform will be prepopulated with the manifesto promises of the 2017-2018 full-time and part-time officers, and give them the opportunity to log progress of each promise along with a completion percentage as they see it (with anything less than 100% meaning they did not manage to complete the task).

This project is inspired by [MySociety's](https://www.mysociety.org) [TheyWorkForYou](https://www.theyworkforyou.com/) project, which aims to keep elected MPs accountable. It is built as coursework for IS52027C: Data, Networks and the Web (2017-18).

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
$ export FLASK_APP=main.py
$ flask db upgrade
```

Make sure you set the following environment variables

```
PASSPHRASE="YourPassphraseForUserReg"
ADMIN_PASS="YourPassphraseForAdmin"
```

## Running project

```
# Enable virtualenv if you killed your terminal instance since the last time you ran this command
$ source venv/bin/activate

# Expose the entry point of our Flask app and run it
$ export FLASK_APP=main.py
$ flask run --host=0.0.0.0 --port=8000
```