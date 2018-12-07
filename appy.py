# William Lu -- DJPM Theodore "Big T" Peters, Ivan "R." Zhang, Adil "Pickle" Gondal, Imad "The Flip-Flop" Belkebir
# SoftDev1 pd07
# P #01: weather there are pokemon??
# 2018-11-2
from urllib import request, parse
import json
import sqlite3
from os import urandom
from random import randint

from flask import Flask, render_template, request, flash, redirect, url_for, make_response, Request

import util.api as api
from util.db_utils import getType

app = Flask(__name__)

app.secret_key = urandom(32)

colors = {'bug':('#3c9950','#1c4b27', 'white'), # coloring to correspond to pokemon types.
          'dark':('#040707','#595978', 'white'),
          'dragon':('#448a95','#62cad9', 'black'),
          'electric':('#e2e32b', '#fafa72', 'black'),
          'fairy':('#961a45','#e91368', 'white'),
          'fighting':('#994025','#ef6239', 'black'),
          'fire':('#fd4b5a','#ab1f24', 'white'),
          'flying':('#4a677d', '#94b2c7', 'black'),
          'ghost':('#33336b', '#4a677d', 'white'),
          'grass':('#147b3d', '#27cb50', 'white'),
          'ground':('#a8702d','#6e491f', 'white'),
          'ice':('#86d2f5', '#d8f0fa', 'black'),
          'normal':('#75525c', '#ca98a6', 'black'),
          'poison':('#5e2d89', '#9b69da', 'black'),
          'psychic':('#a52a6c', '#f77abd', 'black'),
          'rock':('#48190b', '#8b4c35', 'white'),
          'steel':('#82bda9','#60756e', 'white'),
          'water':('#8faffb','#144bc6', 'white')}

@app.route("/")
def home():
    '''landing page'''
    return render_template("home.html", last_loc = get_last_loc(), last_poke = get_last_poke(), capitalize = capitalize)

@app.route("/weather/<city>")
def weather(city):
    '''weather info for a particular city'''
    weather_stuff = api.weather(city.lower())
    map_stuff = api.map(city.lower())
    if weather_stuff != None:
        reduced_types = getType(weather_stuff["main"])
        pokemon = api.poke_list(reduced_types)
        rest = len(reduced_types)
        res = 4
        
        if(rest > 5 and rest%3 == 0):
            res = 3
        elif(rest < 2):
            res = 1
        elif(rest < 4):
            res = 2
        print(res)

        resp = make_response(render_template("weather.html", colors = colors, last_loc = get_last_loc(), last_poke = get_last_poke(), **weather_stuff, types = reduced_types, len_cell = res, pokemon = pokemon, capitalize = capitalize, mapurl = map_stuff))
        resp.set_cookie("last_loc", city.lower()) # adding info on last location
        return resp
    flash("Location does not exit.")
    return redirect("/")
@app.route("/pokeinfo/<name>")
def pokeinfo(name):
    '''information for a specific pokemon'''
    poke_data = api.poke(name.lower())
    if poke_data != None:
        res = make_response(render_template("poke_info.html", data = poke_data, n = name.lower(), colors = colors, last_loc = get_last_loc(), last_poke = get_last_poke(), capitalize = capitalize))
        res.set_cookie("last_poke", name.lower()) # adding info on last pokemon
        return res
    flash("Pokemon does not exist.")
    return redirect("/")

@app.route("/search", methods=["GET"])
def search():
    '''redirects search appropriately based on what was searched for'''
    q = str(request.args.get('q')).lower()
    if q == "william lu":
        return redirect("/williamlu")
    if len(q) > 0 and 'q' in request.args:
        chck = api.poke(q)
        if chck != None:
            return redirect("/pokeinfo/"+q)
        chck = api.weather(q)
        if chck != None:
            return redirect("/weather/"+q)    
    flash("Bad search query.")
    return redirect("/")

@app.route("/random")
def randloc():
    '''random location'''
    lat = randint(-90,90)
    lon = randint(-180,180)
    weather_stuff = api.weather(None, lat, lon)
    map_stuff = api.map(None, lat, lon)
    if weather_stuff != None:
        if weather_stuff["name"]=="":
            weather_stuff["name"]="???"
        reduced_types = getType(weather_stuff["main"])
        pokemon = api.poke_list(reduced_types)
        rest = len(reduced_types)
        res = 4
        
        if(rest > 5 and rest%3 == 0):
            res = 3
        elif(rest < 2):
            res = 1
        elif(rest < 4):
            res = 2
        print(res)

        return render_template("weather.html", colors = colors, last_loc = get_last_loc(), last_poke = get_last_poke(), **weather_stuff, types = reduced_types, len_cell = res, pokemon = pokemon, mapurl = map_stuff, capitalize = capitalize)
    flash("Could not get data on random location.")
    return redirect("/")    

@app.route("/williamlu")
def williamlu():
    '''william who?'''
    return render_template("william_lu.html", colors = colors, last_loc = get_last_loc(), last_poke = get_last_poke(), capitalize = capitalize)

def capitalize(move):
    '''capitalized series of words seperated by either hyphens or spaces'''
    seperate = move.split(" ")
    result = ""
    for move in seperate:
        result += move.capitalize() + " "
    seperate = result[:-1].split("-")
    result = ""
    for move in seperate:
        result += move[0].upper() + move[1:] + " " 
    return result[:-1]

def get_last_poke():
    '''last pokemon accessed by user'''
    return request.cookies.get("last_poke")

def get_last_loc():
    '''last location accessed by user'''
    return request.cookies.get("last_loc")

if __name__ == "__main__":
    app.debug = True
    app.run()
