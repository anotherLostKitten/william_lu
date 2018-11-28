# William Lu -- DJPM Theodore "Big T" Peters, Ivan "R." Zhang, Adil "Pickle" Gondal, Imad "The Flip-Flop" Belkebir
# SoftDev1 pd07
# P #01: weather there are pokemon??
# 2018-11-2
from urllib import request, parse
import json
import sqlite3
import util.api as api

from flask import Flask, render_template

app = Flask(__name__)


        
@app.route("/")
def home():
    return render_template("home.html", **api.weather() )




if __name__ == "__main__":
	app.debug = True
	app.run()
