# retrieves weather data, converts weather info into info about pokemon types, retrieves pokemon data

from urllib import request, parse
import json
import sqlite3

def convert(temp):
    return round((temp-273.15) * 1.8 + 32)

def weather():
    url = request.urlopen("http://api.openweathermap.org/data/2.5/weather?q=Toronto&APPID=1d18700111907e62e27adc5fa89fad1a")
    dict = json.loads(url.read())
   # print (dict)
    icon = dict["weather"][0]["icon"]
    iconUrl="http://openweathermap.org/img/w/" + icon + ".png"
    content = {'img':iconUrl,'name':dict["name"],'expl':dict["weather"][0]["description"],'max' : convert(dict["main"]["temp_max"]),'min': convert(dict["main"]["temp_min"]),'now' : convert(dict["main"]["temp"])}
    return content
