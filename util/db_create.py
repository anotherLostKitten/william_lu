import sqlite3

if __name__ == "__main__":
    DB_FILE = "app.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()


    c.execute("DROP TABLE IF EXISTS data;")
    c.execute("CREATE TABLE data (weather TEXT, type TEXT)")

    data = [["clear sky", "flying,steel"],["clear", "flying,fighting"], ["few clouds", "normal,bug"], ["clouds", "dragon,fairy"], ["scattered clouds", "bug,poison"], ["broken clouds", "dark,ghost,rock"], ["shower rain", "grass,ground"], ["drizzle", "ground,steel"], ["rain", "water,normal"], ["thunderstorm", "electric,psychic"], ["snow", "ice,normal"], ["mist", "psychic,ice"]]

    
    c.executemany("INSERT INTO data VALUES (?,?)", data)
    
    db.commit()
    db.close()
