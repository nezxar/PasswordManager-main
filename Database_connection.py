import sqlite3
from sqlite3 import Connection

class SQL:
    def __init__(self) -> None:
        # self.__db_filename = ".db"
        self.__DB_NAME = "nizar_database"
        self.__TABLE_NAME = "user_info"
        self.conn = self.connect()
    
    def connect(self) -> "Connection": # type: ignore
        try:
            print("Connected to SQLite database.")
            return sqlite3.connect(self.__DB_NAME + '.db')
        except Exception as e:
            print(f"Failed to connect to the database: {e}")

    def create_table(self) -> str:
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS user_info 
                (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                password TEXT,
                email TEXT,
                site_name TEXT,
                encryption_type TEXT
                )
                """)
            self.conn.commit()
            self.conn.close()
            return "Table created successfully."
        except Exception as e:
            return f"Failed to create table: {e}"
    