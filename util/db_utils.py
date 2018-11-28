import sqlite3
import urllib.request
import json

DB_FILE = "app.db"
db = sqlite3.connect(DB_FILE)
c = db.cursor()

def getWeather(city):
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&APPID=60e682c75106d10867a11f4f01d603fc"
    url = urllib.request.Request(api, headers={'User-Agent': 'Mozilla/5.0'})
    url = urllib.request.urlopen(url)
    data = json.loads(url.read())
    return data['weather'][0]['main']


url2 = urllib.request.Request("https://pokeapi.co/api/v2/pokemon", headers={'User-Agent': 'Mozilla/5.0'})
url2 = urllib.request.urlopen(url2)
data2 = json.loads(url2.read())

api = "https://api.openweathermap.org/data/2.5/weather?q=London&APPID=60e682c75106d10867a11f4f01d603fc"
url = urllib.request.Request(api, headers={'User-Agent': 'Mozilla/5.0'})
url = urllib.request.urlopen(url)
data = json.loads(url.read())
print(data)
