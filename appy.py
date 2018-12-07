# William Lu -- DJPM Theodore "Big T" Peters, Ivan "R." Zhang, Adil "Pickle" Gondal, Imad "The Flip-Flop" Belkebir
# SoftDev1 pd07
# P #01: weather there are pokemon??
# 2018-11-2
from urllib import request, parse
import json
import sqlite3
from os import urandom

from flask import Flask, render_template, request, flash, redirect, url_for, session

import util.api as api
from util.db_utils import getType
from util.cap import capitalize

app = Flask(__name__)

app.secret_key = urandom(32)

colors = {'bug':('#3c9950','#1c4b27'),
          'dark':('#040707','#595978'),
          'dragon':('#448a95','#62cad9'),
          'electric':('#fafa72','#e2e32b'),
          'fairy':('#961a45','#e91368'),
          'fighting':('#ef6239','#994025'),
          'fire':('#fd4b5a','#ab1f24'),
          'flying':('#94b2c7','#4a677d'),
          'ghost':('#4a677d','#33336b'),
          'grass':('#27cb50','#147b3d'),
          'ground':('#a8702d','#6e491f'),
          'ice':('#d8f0fa','#86d2f5'),
          'normal':('#ca98a6','#75525c'),
          'poison':('#9b69da','#5e2d89'),
          'psychic':('#f77abd','#a52a6c'),
          'rock':('#8b4c35','#48190b'),
          'steel':('#82bda9','#60756e'),
          'water':('#8faffb','#144bc6')}

@app.route("/")
def home():
    return render_template("home.html", last_loc = get_last_loc(), last_poke = get_last_poke())

@app.route("/weather/<city>")
def weather(city):
    weather_stuff = api.weather(city.capitalize())
    reduced_types = set()
    all_types = weather_stuff['pokemon'][0]['types']
    for t in all_types:
        reduced_types.add(t['type']['name'])
    rest = len(reduced_types)
    res = 4

    if(rest > 5 and rest%3 == 0):
        res = 3
    elif(rest < 2):
        res = 1
    elif(rest < 4):
        res = 2
    print(res)

    return render_template("weather.html", colors = colors, last_loc = get_last_loc(), last_poke = get_last_poke(), **weather_stuff, types = reduced_types, len_cell = res)

@app.route("/pokeinfo/<name>" )
def pokeinfo(name):
    poke_data = get_cache(name.lower())
    for move in poke_data['moves']:
        move['move']['name']=capitalize(move['move']['name'])
    for ability in poke_data['abilities']:
        ability['ability']['name']=capitalize(ability['ability']['name'])
    if poke_data != None:
        return render_template("poke_info.html", data = poke_data, n = name.lower(), colors = colors, last_loc = get_last_loc(), last_poke = set_last_poke(name))
    flash("Pokemon does not exist.")
    return redirect("/")

@app.route("/search", methods=["GET"])
def search():
    q = str(request.args.get('q')).lower()
    if len(q) > 0 and 'q' in request.args:
        chck = get_cache(q)
        if chck != None:
            return redirect("/pokeinfo/"+q)
        chck = api.weather(q)
        if chck != None:
            return redirect("/weather/"+q)
        else:
            return redirect("/")
            
    flash("Bad search query.")
    return redirect("/")

#@app.route("/random")
#def randloc():
#    pass

def add_cache(pokes):
    '''stores each pokemon in a list to cookies'''
    for i in pokes:
        if i["name"].lower() not in session:
            session[i["name"].lower()] = i

def clear_cache():
    '''clears cookies'''
    session.clear()

def get_cache(poke):
    '''if a pokemon desn't exists in cookies, adds to cookies. regardless, returns pokemon data.'''
    poke = poke.lower()
    if poke not in session:
        d = api.poke(poke)
        print(d)
        if d != None:
            add_cache((d,))
        return d
    return session[poke]

def get_last_poke():
    if "last_poke" in session:
        return session["last_poke"]
    return None
def set_last_poke(poke):
    tmp = get_last_poke()
    session["last_poke"] = poke.lower()
    return tmp

def get_last_loc():
    if "last_loc" in session:
        return session["last_loc"]
    return None
def set_last_loc(loc):
    tmp = get_last_loc()
    session["last_loc"] = loc.lower()
    return tmp

if __name__ == "__main__":
	app.debug = True
	app.run()
