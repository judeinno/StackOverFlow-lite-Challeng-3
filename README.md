[![Build Status](https://travis-ci.org/judeinno/StackOverFlow-lite.svg?branch=develop)](https://travis-ci.org/judeinno/StackOverFlow-lite)
[![Coverage Status](https://coveralls.io/repos/github/judeinno/StackOverFlow-lite/badge.svg?branch=API)](https://coveralls.io/github/judeinno/StackOverFlow-lite?branch=API)
[![Maintainability](https://api.codeclimate.com/v1/badges/fe0c1562dfa5dd20415c/maintainability)](https://codeclimate.com/github/judeinno/StackOverFlow-lite/maintainability)

# StackOverFlow-lite

This is a question answer app that allows users to ask questions and as well give replys.
it also allows a users to vote for a question and also comment on it

# Main requirements include:
> 1. [git](https://git-scm.com/)
> 2. [python](https://docs.python.org/) 
> 3. [pip](https://pypi.python.org/pypi/pip) 
> 4. [virtualenv](https://virtualenv.pypa.io/en/stable/) 

# Getting Started
1. Clone the project

`git clone https://github.com/judeinno/StackOverFlow-lite.git`

2. Create a virtual environment using `virtualenv` and activate it.

`virtualenv venv`
`venv\Scripts\Activate`

3. Install packages using `pip install -r requirements.txt`

4. Run the app by running `run.py`

`python run.py`


# Project Link
__Interface__
The link to the pages hosted on gh-pages is:
 https://judeinno.github.io/StackOverFlow-lite/templetes/index.html

The link to git hub feature branch with the code is:
https://github.com/judeinno/StackOverFlow-lite/tree/feat/UI-templetes

__API endpoints__

The link to the git hub branch with the code is:
https://github.com/judeinno/StackOverFlow-lite/tree/API


The link to the hosted apis on heroku:
https://mystacklite-api-heroku.herokuapp.com/api/v1/questions

 # Features
__interface__
- Users can create an account and log in.
- The users can ask questions on home page.
- User can view recently asked questions.
- User can vote up and vote down an answer
- User can comment on an answer

__API endpoints__

| End Point                                           | Verb |Use                                   |
| ----------------------------------------------------|------|--------------------------------------|
|`/api/v1/`                                           |GET   |API prefix                            |
|`/api/v1/questions`                                  |GET   |Gets a list of Questions              |
|`/api/v1/questions`                                  |POST  |Post a question                       |
|`/api/v1/questions/<int:qn_id>`                      |GET   |Gets a Question resource of a given ID|
|`/api/v1.0/questions/<int:qn_id>/answers`           |POST  |Adds a an answer to a question        |


# Built With
__interface__
- HTML5
- CSS

__API endpoints__
- Python 3
- Flask
- Flask restful

# Prerequisites
- HTML 5
- Internet

# Authors
Atuhaire Jude Innocent

# Licensing

The app is opensource hence free to all users

- Web browser with support for HTML5
- Internet connection