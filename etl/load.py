import psycopg2
import time
from db import connect_to_db
from extract import fetch_crypto_prices


def insert_crypto_prices():
    """Continuously fetch and insert crypto prices into the database."""
    while True:
        conn = connect_to_db()
        if conn is None:
            return

        try:
            cur = conn.cursor()
            data = fetch_crypto_prices()

            if data:
                insert_query = """
                INSERT INTO crypto_prices (currency, price_usd)
                VALUES (%s, %s);
                """
                for currency, details in data.items():
                    cur.execute(insert_query, (currency, details['usd']))

                conn.commit()
                print("New crypto prices inserted.")

            cur.close()
            conn.close()

        except Exception as e:
            print("Error inserting data:", e)

        # Wait 30 seconds before fetching new data
        time.sleep(30)

if __name__ == "__main__":
    print("Starting real-time price tracking...")
    insert_crypto_prices()
