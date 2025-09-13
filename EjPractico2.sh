#!/bin/bash
mkdir TP2-IDS
cd TP2-IDS
mkdir .venv
mkdir static
cd static
mkdir css
mkdir images
cd ..
mkdir templates
touch app.py
pipenv install flask
pipenv shell
export FLASK_APP=app.py
export FLASK_DEBUG=1