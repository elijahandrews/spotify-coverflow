#!/usr/bin/env bash

pip install -r requirements.txt
# the version in pip is out of date
pip install git+https://github.com/plamere/spotipy.git --upgrade

# require to create .cache_<USER> file to store spotify credentials
python -m spotify_coverflow

flask --app web_app run --port=1973 --host=0.0.0.0
