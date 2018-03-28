# The Work For GoldSU

## Overview of project

Born from a desire to better understand how promises are carried through, They Work For GoldSU is a platform for elected officials at Goldsmiths Students' Union to keep a meaningful log of their progress throughout the year. The platform will be prepopulated with the manifesto promises of the 2017-2018 full-time and part-time officers, and give them the opportunity to log progress of each promise along with a completion percentage as they see it (with anything less than 100% meaning they did not manage to complete the task).

This project is inspired by [MySociety's](https://www.mysociety.org) [TheyWorkForYou](https://www.theyworkforyou.com/) project, which aims to keep elected MPs accountable. It is built as coursework for IS52027C: Data, Networks and the Web (2017-18), and born from cynicism as a member of the Students' Union.

## Technical overview

* Data
  * Table of officers (include field for resigned)
  * Table of manifesto promises, against officers
  * Table of updates, against promises
  * Table of users (admin + officers only)
* Users
  * Admin
    * Generate officers
    * Generate users, and link to an officer
    * Generate promises and link to users
  * Officer
    * Can CRUD updates against promises
    * Each update gives opportunity for a % change
    * Can update a photo
* Views
  * Home (list of officers)
  * Login / lost password
  * Single officer
    * Logged in
    * Logged out
  * New general update
  * New manifesto update


## Technical Requirements

* it is a flask app
  * there is more than one route and more than one view
* the html is rendered using jinja templates
  * the jinja templates include some control structure(S) e.g. if/else, for/endfor
* it includes one or more forms
  * the forms have some validation
  * there are useful feedback messages to the user
  * using wtforms is not required but is recommended
* it has a database backend that implements CRUD operations
  * the database can be mysql or mongodb
  * the create & update operations take input data from a form or forms
  * using sqlalchemy is not required but will attract credit
* there is user authentication (i.e. logins)
  * the login process uses sessions
  * passwords should be stored as hashes
  * using a salt is not required but is recommended
  * there is a way to logout
  * use of flask-login is not required but is recommended
* there is a basic api i.e. content can be accessed as json via http methods
  * it should be clear how to access the api (this could include comments in code)
  * additional credit will be given for an api that implements get,post,push and delete
  * use of flask-restful is not required but is recommended