from db import connect_to_db

def create_crypto_table():
    """Create the crypto_prices table if it doesn't exist."""
    conn = connect_to_db()
    if conn is None:
        return

    try:
        cur = conn.cursor()
        create_table_query = """
        CREATE TABLE IF NOT EXISTS crypto_prices (
            id SERIAL PRIMARY KEY,
            currency TEXT NOT NULL,
            price_usd NUMERIC(10, 4) NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        cur.execute(create_table_query)
        conn.commit()
        print("Table `crypto_prices` created successfully.")
        cur.close()
        conn.close()

    except Exception as e:
        print("Error creating table:", e)

if __name__ == "__main__":
    create_crypto_table()
