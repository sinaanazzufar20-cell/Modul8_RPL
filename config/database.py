import mysql.connector
from mysql.connector import Error
class Database:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.database = "db_perpustakaan_rpl"

    def get_connection(self):
        try:
            conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            return conn
        except mysql.connector.Error as err:
            print(f"Error koneksi database: {err}")
            return None