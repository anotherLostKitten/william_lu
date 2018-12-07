# retrieves weather data, converts weather info into info about pokemon types, retrieves pokemon data

from urllib import request, parse
from urllib.error import HTTPError #error handling for bad api call
from random import sample #needed to get random pokemons
import json
import sqlite3

from util.db_utils import getType
from util.cap import capitalize #capitalizes names 

def getkey(keyfile):
    f = open(keyfile, 'r')
    l = f.read().split('\n')
    f.close()
    return l[0]

weatherkey = getkey("util/keys.txt") #gets API key 

#converts weather from Kelving to Farenheit
def convert(temp):
    return round((temp-273.15) * 1.8 + 32)
def weather(city):
    try:
        site= "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&APPID=" + weatherkey 
        url = request.urlopen(site)
        dict = json.loads(url.read())
        # print (dict)
        icon = dict["weather"][0]["icon"]
        iconUrl="http://openweathermap.org/img/w/" + icon + ".png" #gets weather icon
        input = dict['weather'][0]['main']
        result = getType(input.lower()) #gets pokemon type based on weather
        pokelist = [poke(i['name']) for i in sample(result,9)] #9 random pokemons based on weather type
        for p in pokelist:
            p[p['name']] = capitalize(p['name']) #capitalized and removes hyphens from names
        content = {'img':iconUrl,'name':dict["name"],'expl':dict["weather"][0]["description"],'max' : convert(dict["main"]["temp_max"]),'min': convert(dict["main"]["temp_min"]),'now' : convert(dict["main"]["temp"]),'pokemon': pokelistp} #makes app.py more readable
        return content
    except HTTPError:
        return None

def poke(poke = ''):
    poke = poke.lower()
    try:
        url = "https://pokeapi.co/api/v2/pokemon/"
        url = url + poke
        cri = request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        stuff = request.urlopen(cri) # GETS STUFF
        js = stuff.read() # gets info from urlopen
        jason = json.loads(js)
        if(poke == ''):
            return jason["results"]
        return jason
    except HTTPError:
        return None
