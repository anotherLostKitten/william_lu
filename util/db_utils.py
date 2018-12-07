import sqlite3
import urllib.request
import json

def getType(weather):
    #print(weather)
    DB_FILE = "app.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    db.text_factory = str
    command = "SELECT data.type FROM data WHERE data.weather = \'" + weather.lower() + "\'"
    c.execute(command)
    ptype = c.fetchall()[0][0].split(",")
    print(ptype)
    return ptype

