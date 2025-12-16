import sqlite3
import json

class Database:
    def __init__(self, database_name="Wavelength.db"):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()
        self._make_table()

    def _make_table(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Wavelength(
            playerdata TEXT NOT NULL
            );""")
        
    def add_playerdata(self, playerdata):
        playerdata_json = json.dumps(playerdata)
        self.cursor.execute(
            "INSERT INTO Wavelength (playerdata) VALUES (?);",
            (playerdata_json,)
        )
        self.connection.commit()
        
    def get_all_playerdata(self):
        self.cursor.execute("SELECT * FROM Wavelength;")
        rows = self.cursor.fetchall()
        return [json.loads(row[0]) for row in rows]
    
    def close(self):
        self.connection.close()