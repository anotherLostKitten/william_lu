# William Lu -- DJPM Theodore "Big T" Peters, Ivan "R." Zhang, Adil "Pickle" Gondal, Imad "The Flip-Flop" Belkebir
# SoftDev1 pd07
# P #01: weather there are pokemon??
# 2018-11-2
from urllib import request, parse
import json
import sqlite3

from flask import Flask, render_template

app = Flask(__name__)

def convert(temp):
    return round((temp-273.15) * 1.8 + 32)
        
@app.route("/")
def home():
    url = request.urlopen("http://api.openweathermap.org/data/2.5/weather?q=Toronto&APPID=1d18700111907e62e27adc5fa89fad1a")
    dict = json.loads(url.read())
   # print (dict)
    icon = dict["weather"][0]["icon"]
    iconUrl="http://openweathermap.org/img/w/" + icon + ".png"

    return render_template("home.html", img = iconUrl,name=dict["name"] , expl = dict["weather"][0]["description"],max =convert(dict["main"]["temp_max"]),min = convert(dict["main"]["temp_min"]),now =convert(dict["main"]["temp"]))




if __name__ == "__main__":
	app.debug = True
	app.run()
