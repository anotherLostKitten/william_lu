# William Lu -- DJPM Theodore "Big T" Peters, Ivan "R." Zhang, Adil "Pickle" Gondal, Imad "The Flip-Flop" Belkebir
# SoftDev1 pd07
# P #01: weather there are pokemon??
# 2018-11-2
from urllib import request, parse
import json
import sqlite3
import util.api as api

from flask import Flask, render_template

app = Flask(__name__)
        
@app.route("/")
def home():
    return render_template("home.html", **api.weather('London'))

@app.route("/pokedex/")
def pokedex():
    p_data = api.poke()
    new_pokemons = []
    _c = 0
    for p in p_data:
        if(_c > 10):
            break
        add_this = api.poke(p['name'])
        add_this['name'] = add_this['name'].capitalize()
        new_pokemons.append(add_this)
        _c += 1
    return render_template("poke_data.html", pokes = new_pokemons )
#request.form['pokemon']
@app.route("/pokeinfo/<name>" )
def pokeinfo(name):
    poke_data = api.poke(name)
    
    return render_template("home.html", **api.weather('London'))


if __name__ == "__main__":
	app.debug = True
	app.run()
