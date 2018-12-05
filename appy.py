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

@app.route("/")
def home():
    return render_template("home.html", **api.weather('Brooklyn'))

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
