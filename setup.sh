#!/bin/bash

# install dependencies
pip install -r requirements.txt

# Run django commands
python manage.py migrate
python manage.py runserver
