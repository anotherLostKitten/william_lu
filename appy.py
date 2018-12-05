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

app = Flask(__name__)

app.secret_key = urandom(32)

colors = {'bug':(0x3c9950,0x1c4b27),
          'dark':(0x040707,0x595978),
          'dragon':(0x448a95,0x62cad9),
          'electric':(0xe2e32b,0xfafa72),
          'fairy':(0x961a45,0xe91368),
          'fighting':(0xef6239,0x994025),
          'fire':(0xfd4b5a,0xab1f24),
          'flying':(0x94b2c7,0x4a677d),
          'ghost':(0x4a677d,0x33336b),
          'grass':(0x27cb50,0x147b3d),
          'ground':(0xa8702d,0x6e491f),
          'ice':(0xd8f0fa,0x86d2f5),
          'normal':(0xca98a6,0x75525c),
          'poison':(0x9b69da,0x5e2d89),
          'psychic':(0xf77abd,0xa52a6c),
          'rock':(0x8b4c35,0x48190b),
          'steel':(0x82bda9,0x60756e),
          'water':(0x8faffb,0x144bc6)}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/wtest")
def wtest():
    return render_template("weather.html")
# @app.route("/pokedex/")
# def pokedex():
#     p_data = api.poke()
#     new_pokemons = []
#     _c = 0
#     for p in p_data:
#         if(_c > 20):
#             break
#         add_this = api.poke(p['name'])
#         add_this['name'] = add_this['name'].capitalize()
#         new_pokemons.append(add_this)
#         _c += 1
#     return render_template("poke_data.html", pokes = new_pokemons )
# request.form['pokemon']
@app.route("/pokeinfo/<name>" )
def pokeinfo(name):
    poke_data = get_cache(name.lower())

    return render_template("willaim0.html", data = poke_data, n = name.lower())


@app.route("/test" )
def pokeinfo_info():

    return render_template("willaim.html")

@app.route("/search", methods=["GET"])
def search():
    q = str(request.args.get("q")).lower()
    if len(q) > 0:
        chck = get_cache(q)
        if chck != None:
            return redirect("/pokeinfo/"+q)
        chck = api.weather(q)
        if chck != None:
            return redirect("/wtest")
    return redirect("/")
#   print(request.args)
#   return redirect("/pokeinfo/"+str(request.args.get("q")))

def add_cache(pokes):
    '''stores each pokemon in a list to cookies'''
    for i in pokes:
        if i["name"].lower() not in session:
            session[i["name"].lower()] = i
            
def clear_cache():
    '''clears cookies'''
    session.clear()
    
def get_cache(poke):
    poke = poke.lower()
    '''if a pokemon desn't exists in cookies, adds to cookies. regardless, returns pokemon data.'''
    if poke not in session:
        d = api.poke(poke)
        print(d)
        if d != None:
            add_cache((d,))
        return d
    return session[poke]

if __name__ == "__main__":
	app.debug = True
	app.run()
