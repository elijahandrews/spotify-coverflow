#!/usr/bin/env bash

pip install -r requirements.txt
# the version in pip is out of date 
pip install git+https://github.com/plamere/spotipy.git --upgrade

flask --app web_app run
