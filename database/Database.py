import psycopg2
import os
from psycopg2.extras import DictCursor
from dotenv import load_dotenv

load_dotenv()


class Database:
    def __init__(self):
        self.connection = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            cursor_factory=DictCursor
        )
        
    def get_cursor(self):
        return self.connection.cursor()

    def close(self):
        self.connection.close()

    def __enter__(self):
        return self.get_cursor()

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
