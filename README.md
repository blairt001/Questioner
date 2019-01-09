[![Build Status](https://travis-ci.org/blairt001/Questioner.svg?branch=develop)](https://travis-ci.org/blairt001/Questioner)[![Coverage Status](https://coveralls.io/repos/github/blairt001/Questioner/badge.svg?branch=develop)](https://coveralls.io/github/blairt001/Questioner?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/2a72a608512cb9809c24/maintainability)](https://codeclimate.com/github/blairt001/Questioner/maintainability)


## Heroku Link

#  Sample Tasks
 
 >  **[Pivotal Tracker Board Stories](https://www.pivotaltracker.com/n/projects/2235680)**


# Project Overview
Questioner is a crowd-source questions for a meetup. It helps the meetup organizer prioritize questions to be answered. Other users can vote on asked questions and they bubble to the top or to the bottom of the log.

## Questioner API Endpoints

| Method        |       Endpoint                              |         Description                           |
| ------------- |       -------------                         |         -------------                         |
| `GET`         | `/api/v1/meetups/upcoming`                  |   Gets all meetups records                    |
| `GET`         | `/api/v1/meetups/<meetup-id>`               |   Get a specific meetup record                |
| `POST`        | `/api/v1/meetups`                           |   Create a meetup record                      |
| `POST`        | `/api/v1/questions`                         |   Create a question record                    |
| `POST`        | `/api/v1/users/registration`                |   Register a user                             |
| `POST`        | `/api/v1/users/login`                       |   Sign in a User                              |
| `POST`        | `/api/v1/meetups/<meetup-id/rsvps>`         |   User respond to a meetup                    |
| `PATCH`       | `/api/v1/questions/<questions-id>/upvote`   |   vote on a meetup question                   |
| `PATCH`       | `/api/v1/questions/<questions-id/downvote`  |   vote on a meetup question                   |



# Setting up your system

Install python3+ version.

# Getting Started

Clone the repository :

`git clone https://github.com/blairt001/Questioner.git`

cd into the repository

Activate virtualenv: `source venv/bin/activate`


## Install requirements.txt

```
pip install -r requirements.txt
```

## Running the Application

Follow the following procedures:

```
export  FLASK_ENV=development
```

```
export FLASK_APP=manage.py
```

```
python manage.py runserver
```

## Unit Testing
 On the terminal execute `python -m pytests`

### Testing API Endpoints:
Use [Postman](https://learning.getpostman.com/docs/postman/launching_postman/installation_and_updates/)

### License
[MIT LICENSE](https://github.com/blairt001/Questioner/blob/develop/LICENSE)

## Credits
[Andela](https://andela.com/)

## Developer
Tony Blair Okoth

