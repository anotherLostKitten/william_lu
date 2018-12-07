# William Lu -- DJPM Theodore "Big T" Peters, Ivan "R." Zhang, Adil "Pickle" Gondal, Imad "The Flip-Flop" Belkebir
# SoftDev1 pd07
# P #01: weather there are pokemon??
# 2018-11-2
from urllib import request, parse
import json
import sqlite3

from flask import Flask, render_template, request, flash, redirect, url_for, make_response, Request

import util.api as api
from util.db_utils import getType
from util.cap import capitalize

app = Flask(__name__)

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

        resp = make_response(render_template("weather.html", colors = colors, last_loc = get_last_loc(), last_poke = get_last_poke(), **weather_stuff, types = reduced_types, len_cell = res, pokemon = pokemon))
        resp.set_cookie("last_loc", city.lower())
        return resp
    flash("Location does not exit.")
    return redirect("/")
@app.route("/pokeinfo/<name>" )
def pokeinfo(name):
    poke_data = api.poke(name.lower())
    for move in poke_data['moves']:
        move['move']['name']=capitalize(move['move']['name'])
    for ability in poke_data['abilities']:
        ability['ability']['name']=capitalize(ability['ability']['name'])
    if poke_data != None:
        res = make_response(render_template("poke_info.html", data = poke_data, n = name.lower(), colors = colors, last_loc = get_last_loc(), last_poke = get_last_poke()))
        res.set_cookie("last_poke", name.lower())
        return res
    flash("Pokemon does not exist.")
    return redirect("/")

@app.route("/search", methods=["GET"])
def search():
    q = str(request.args.get('q')).lower()
    if len(q) > 0 and 'q' in request.args:
        chck = api.poke(q)
        if chck != None:
            return redirect("/pokeinfo/"+q)
        chck = api.weather(q)
        if chck != None:
            return redirect("/weather/"+q)
        else:
            return redirect("/")
            
    flash("Bad search query.")
    return redirect("/")

@app.route("/random")
def randloc():
    pass

def get_last_poke():
    return capitalize(request.cookies.get("last_poke"))

def get_last_loc():
    return capitalize(request.cookies.get("last_loc"))

if __name__ == "__main__":
	app.debug = True
	app.run()
