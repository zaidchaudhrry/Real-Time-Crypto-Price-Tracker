🚀 Real-Time Crypto Price Tracker
A real-time cryptocurrency price tracker that fetches live prices for Bitcoin, Ethereum, and Cardano, stores them in a PostgreSQL database, and displays price trends using FastAPI & Streamlit.

📌 Features
✅ Real-Time Crypto Data – Fetches latest prices every 60 seconds
✅ PostgreSQL Storage – Saves historical price data
✅ FastAPI Backend – Provides latest prices via REST API
✅ Streamlit Dashboard – Visualizes price trends
✅ Retry Logic – Handles API rate limits (CoinGecko)
✅ Docker Support – (Optional) for easy deployment

📦 Tech Stack
Python 🐍
FastAPI ⚡ (Backend API)
PostgreSQL 🛢 (Database)
Streamlit 📊 (Dashboard)
Docker 🐳 (Deployment - Optional)

🚀 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/zaidchaudhrry/Real-Time-Crypto-Price-Tracker.git
cd Real-Time-Crypto-Price-Tracker

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Set Up PostgreSQL Database
Create a database in PostgreSQL:

CREATE DATABASE etl_db;

Create the table:

CREATE TABLE crypto_prices (
    id SERIAL PRIMARY KEY,
    currency VARCHAR(20),
    price_usd DECIMAL(18,8),
    timestamp TIMESTAMP DEFAULT NOW()
);
1️⃣ Start the FastAPI Backend:
uvicorn api.main:app --reload

2️⃣ Start the Streamlit Dashboard:
streamlit run dashboard/app.py

📌 Future Improvements
🔹 Add WebSocket support for real-time price updates
🔹 Store more cryptocurrencies & fiat currencies
🔹 Deploy to AWS, Heroku, or Railway.app
🔹 Improve UI with Plotly charts & Moving Averages

💡 Contributing
Pull requests are welcome!
Fork the repo, make changes, and submit a PR.
