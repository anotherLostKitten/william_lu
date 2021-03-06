# retrieves weather data, converts weather info into info about pokemon types, retrieves pokemon data

from urllib import request, parse
from urllib.error import HTTPError # error handling for bad api calls
from random import sample, shuffle # needed to get random pokemons
import json
import sqlite3

from util.db_utils import getType

def getkey(keyfile):
    '''retrives api keys based on file name'''
    try:
        f = open(keyfile, 'r')
    except FileNotFoundError:
        print("Missing key file, using default value...")
        f = open(keyfile+"_default", 'r')
    l = f.read().split('\n')
    f.close()
    return l[0]

weatherkey = getkey("util/keys.txt") #gets API key 
mapkey = getkey("util/mapkeys.txt")

#converts weather from Kelving to Farenheit
def convert(temp):
    '''kelvin > ferienheit'''
    return round((temp-273.15) * 1.8 + 32)

def weather(city, lat = False, lon = False):
    '''weather info for a city or lattitude & longitude values'''
    try:
        site= "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&APPID=" + weatherkey if not lon else "http://api.openweathermap.org/data/2.5/weather?lon=" + str(lon) + "&lat=" + str(lat) + "&APPID=" + weatherkey
        print(site)
        url = request.urlopen(site)
        wdict = json.loads(url.read())
        # print (dict)
        iconUrl="http://openweathermap.org/img/w/" + wdict["weather"][0]["icon"] + ".png"
        winfo = wdict["weather"][0]["main"]
        content = {"img":iconUrl,"name":wdict["name"],"expl":wdict["weather"][0]["description"],"max":convert(wdict["main"]["temp_max"]),"min":convert(wdict["main"]["temp_min"]),"now":convert(wdict["main"]["temp"]),"main":winfo}
        return content
    except HTTPError:
        return None

def poke_list(types):
    '''randomizez a list of 9 pokemon of certain types'''
    result = poke_list_full(types)
    shuffle(result)
    pokemons = []
    for i in result:
        tst = poke(i['name'])
        if tst['sprites']['front_default'] != None:
            pokemons.append(tst)
            if len(pokemons) >= 9: # change 9 for more or less pokemon
                break
    return pokemons

def poke_list_full(ptype):
    '''all pokemon of certain types'''
    print(ptype)
    pokemon = []
    for type in ptype:
        url = request.Request("https://pokeapi.co/api/v2/type/" + type, headers={'User-Agent': 'Mozilla/5.0'})
        url = request.urlopen(url)
        data = json.loads(url.read())
        data = data["pokemon"]
        for poke in data:
            pokemon.append(poke["pokemon"])
    #print(pokemon)
    return pokemon


def poke(poke = ''):
    '''info on a specific pokemon'''
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

def map(city, lat = False, lon = False):
    '''map api i need to make a api knowledge base post on probably'''
    q = "https://open.mapquestapi.com/staticmap/v5/map?key="+mapkey+"&center="+ (city if not lon else str(lon) + "," + str(lat)) +"&size=500,200@2x&type=light"
    print(q)
    return q

