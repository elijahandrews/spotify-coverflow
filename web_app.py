from flask import Flask, render_template
from spotify_coverflow import get_token, get_img

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", img_src=get_img(get_token()))
