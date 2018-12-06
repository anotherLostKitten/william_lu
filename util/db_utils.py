import sqlite3
import urllib.request
import json

def getType(weather):
    #print(weather)
    DB_FILE = "app.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    db.text_factory = str
    command = "SELECT data.type FROM data WHERE data.weather = \'" + weather + "\'"
    c.execute(command)
    ptype = c.fetchall()[0][0].split(",")
    pokemon = []

    for type in ptype:
        url = urllib.request.Request("https://pokeapi.co/api/v2/type/" + type, headers={'User-Agent': 'Mozilla/5.0'})
        url = urllib.request.urlopen(url)
        data = json.loads(url.read())
        data = data['pokemon']
        for poke in data:
            pokemon.append(poke['pokemon'])

    return pokemon
