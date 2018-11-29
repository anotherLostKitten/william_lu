import sqlite3
import urllib.request
import json

def getType(weather):
    DB_FILE = "app.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    db.text_factory = str
    command = "SELECT data.type FROM data WHERE data.weather = \'" + weather + "\'"
    c.execute(command)
    type = c.fetchall()
    return type

type = getType('rain')
url2 = urllib.request.Request("https://pokeapi.co/api/v2/type/" + type[0][0], headers={'User-Agent': 'Mozilla/5.0'})
url2 = urllib.request.urlopen(url2)
data2 = json.loads(url2.read())

print(data2)
