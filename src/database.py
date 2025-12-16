import sqlite3
import json

class Database:
    def __init__(self, database_name="Wavelength.db"):
        self.connection = sqlite3.connection()
        self.cursor = self.connection.cursor()
        self._make_table()

    def _make_table(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Wavelength(
            playerdata TEXT NOT NULL
            );""")