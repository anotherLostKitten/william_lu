import sqlite3
import urllib.request
import json

def getType(weather):
    print(weather)
    DB_FILE = "app.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    db.text_factory = str
    command = "SELECT data.type FROM data WHERE data.weather = \'" + weather + "\'"
    c.execute(command)
    ptype = c.fetchall()
    print(ptype)
    url2 = urllib.request.Request("https://pokeapi.co/api/v2/type/" + ptype[0][0], headers={'User-Agent': 'Mozilla/5.0'})
    url2 = urllib.request.urlopen(url2)
    data2 = json.loads(url2.read())
    
    return data2
