import sqlite3

DB_FILE = "app.db"
db = sqlite3.connect(DB_FILE)
c = db.cursor()

command = "CREATE TABLE pokemon (weather TEXT, pokemon TEXT)"
c.execute(command)

data = [["clear sky", "drifloon"], ["few clouds", "chandelure"], ["scattered clouds", "espeon"], ["broken clouds", "wobbuffet"], ["shower rain", "piplup"], ["drizzle", "squirtle"], ["rain", "magikarp"], ["thunderstorm", "pikachu"], ["snow", "cubchoo"], ["mist", "umbreon"]]

c.executemany("INSERT INTO pokemon VALUES (?,?)", data)

db.commit()
db.close()
