#!/bin/sh
#export FLASK_APP=manage.py
#source $(pipenv --venv)/bin/activate
#flask run -h 0.0.0.0
gunicorn -b 0.0.0.0:5000 app:app

