from flask import Flask, render_template
import TMDB

import requests
from pprint import pprint
import json

app = Flask(__name__)

@app.route("/")
def index():
    # api = TMDB.TMDB("eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkMzY1NjJkNjM1N2M0ZDZjYzI0ZjM3ZTZhM2VjMDVmNiIsInN1YiI6IjY0ZGM3Mzc1ZDEwMGI2MTRiMmVlYjVkZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.CdyaHhnNE8ORBP5Rz6Xv5V5pP2bbYmSYkuvFyLMlkfs") # tokenは発行された文字列を代入

    title = "君たちはどう生きるか"
    res = TMDB.TMDB.search_movies_jp(title)

    poster_path = res['results'][0]['poster_path']


    return render_template("index.html", title=title, poster_path=poster_path)

@app.route("/map")
def map():

    return render_template("map.html")

if __name__ == "__main__":
    app.run()