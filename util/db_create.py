import sqlite3

DB_FILE = "app.db"
db = sqlite3.connect(DB_FILE)
c = db.cursor()


c.execute("DROP TABLE IF EXISTS data;")
c.execute("CREATE TABLE data (weather TEXT, type TEXT)")

data = [["clear sky", "flying"], ["few clouds", "normal"], ["clouds", "dragon"], ["scattered clouds", "bug"], ["broken clouds", "dark"], ["shower rain", "grass"], ["drizzle", "ground"], ["rain", "water"], ["thunderstorm", "electric"], ["snow", "ice"], ["mist", "psychic"]]

c.executemany("INSERT INTO data VALUES (?,?)", data)

db.commit()
db.close()
