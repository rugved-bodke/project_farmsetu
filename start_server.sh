#!/bin/bash
python3.8 manage.py makemigrations hub
python3.8 manage.py migrate hub
python3.8 manage.py makemigrations
python3.8 manage.py migrate
python3.8 manage.py runserver 0:8000