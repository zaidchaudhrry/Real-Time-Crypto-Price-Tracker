from fastapi import FastAPI
import psycopg2
import os
import subprocess
import threading
from dotenv import load_dotenv
import sys
# Load environment variables
load_dotenv()

# Database connection details
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT")

# Initialize FastAPI app
app = FastAPI()

# Function to get the latest prices from PostgreSQL
def get_latest_prices():
    """Fetch only the latest prices per currency from the database."""
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        cur = conn.cursor()

        query = """
        SELECT DISTINCT ON (currency) currency, price_usd, timestamp
        FROM crypto_prices
        ORDER BY currency, timestamp DESC;
        """
        cur.execute(query)
        rows = cur.fetchall()
        cur.close()
        conn.close()

        # Convert rows to JSON format
        prices = [{"currency": row[0], "price_usd": row[1], "timestamp": row[2]} for row in rows]
        return prices

    except Exception as e:
        return {"error": str(e)}

# API endpoint to fetch latest prices
@app.get("/latest-prices")
def latest_prices():
    return get_latest_prices()

# Function to run `load.py` in a background thread
def start_etl_process():
    subprocess.Popen([sys.executable, "../etl/load.py"])

# Start the ETL process when FastAPI starts
etl_thread = threading.Thread(target=start_etl_process, daemon=True)
etl_thread.start()
