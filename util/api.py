# retrieves weather data, converts weather info into info about pokemon types, retrieves pokemon data

from urllib import request, parse
from random import choice
import json
import sqlite3
from util.db_utils import getType


def convert(temp):
    return round((temp-273.15) * 1.8 + 32)

def weather(city):
    site= "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&APPID=1d18700111907e62e27adc5fa89fad1a"
    url = request.urlopen(site)
    dict = json.loads(url.read())
   # print (dict)
    icon = dict["weather"][0]["icon"]
    iconUrl="http://openweathermap.org/img/w/" + icon + ".png"
    input = dict['weather'][0]['main']
    result = getType(input.lower())
    content = {'img':iconUrl,'name':dict["name"],'expl':dict["weather"][0]["description"],'max' : convert(dict["main"]["temp_max"]),'min': convert(dict["main"]["temp_min"]),'now' : convert(dict["main"]["temp"]),'pokemon':choice(result['pokemon'])['pokemon']['name']}
    return content

def poke(poke = ''):
    url = "https://pokeapi.co/api/v2/pokemon/"
    url = url + poke
    cri = request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    stuff = request.urlopen(cri) # GETS STUFF 
    js = stuff.read() # gets info from urlopen
    jason = json.loads(js)
    if(poke == ''):
        return jason["results"]
    return jason
