import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get PostgreSQL credentials from .env
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT")

def connect_to_db():
    """Connect to PostgreSQL and return connection."""
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        print("Connected to PostgreSQL")
        return conn
    except Exception as e:
        print("Error connecting to database:", e)
        return None
