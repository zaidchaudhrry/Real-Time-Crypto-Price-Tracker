# 🚀 Real-Time Crypto Price Tracker

A real-time cryptocurrency price tracker that fetches live prices for **Bitcoin, Ethereum, and Cardano**, stores them in a **PostgreSQL database**, and displays price trends using **FastAPI & Streamlit**.

---

## 📌 Features

👉 **Real-Time Crypto Data** – Fetches the latest prices every 60 seconds  
👉 **PostgreSQL Storage** – Saves historical price data  
👉 **FastAPI Backend** – Provides latest prices via REST API  
👉 **Streamlit Dashboard** – Visualizes price trends  
👉 **Retry Logic** – Handles API rate limits (CoinGecko)  
👉 **Docker Support** – (Optional) for easy deployment  

---

## 💪 Tech Stack

| Technology    | Purpose                                  |
|--------------|------------------------------------------|
| **Python** 🐍 | Core programming language               |
| **FastAPI** ⚡ | Backend API for serving live prices   |
| **PostgreSQL** 👢 | Database for storing price data    |
| **Streamlit** 📊 | Interactive dashboard visualization  |
| **Docker** 🐳 | Deployment (Optional)                   |

---

## 📂 Project Structure

```
📁 Real-Time-Crypto-Price-Tracker/
│── api/
│   ├── main.py        # FastAPI backend to fetch and serve price data
│── dashboard/
│   ├── app.py         # Streamlit dashboard for data visualization
│── database/
│   ├── db.py          # PostgreSQL connection setup
│── scripts/
│   ├── fetch_prices.py # Fetches latest crypto prices
│── data/              # Directory for storing CSV exports
│── .env               # Environment variables for database credentials
│── requirements.txt   # Required Python dependencies
│── Dockerfile         # Docker setup (optional)
│── README.md          # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/zaidchaudhrry/Real-Time-Crypto-Price-Tracker.git
cd Real-Time-Crypto-Price-Tracker
```

### 2️⃣ Set Up a Virtual Environment (Recommended)
```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# OR
.venv\Scripts\activate     # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🗂️ Setting Up PostgreSQL Database

### 4️⃣ Create a Database
Ensure **PostgreSQL** is running and create the database:
```sql
CREATE DATABASE crypto_db;
```

### 5️⃣ Create the Table
Run the following SQL command to create a table for storing price data:
```sql
CREATE TABLE crypto_prices (
    id SERIAL PRIMARY KEY,
    currency VARCHAR(20),
    price_usd DECIMAL(18,8),
    timestamp TIMESTAMP DEFAULT NOW()
);
```

---

## 🚀 Running the Project

### 1️⃣ Start the FastAPI Backend
```bash
uvicorn api.main:app --reload
```
- This will launch a REST API that fetches and serves live crypto prices.

### 2️⃣ Start the Streamlit Dashboard
```bash
streamlit run dashboard/app.py
```
- This will open an interactive web-based dashboard to visualize the latest price trends.

---

## 📊 Future Improvements

- 🔹 **Add WebSocket support** for real-time price updates  
- 🔹 **Expand to more cryptocurrencies & fiat currencies**  
- 🔹 **Deploy to AWS, Heroku, or Railway.app**  
- 🔹 **Enhance UI with Plotly charts & Moving Averages**  

---

## 💜 License

This project is licensed under the **MIT License**.

---

## 🤝 Contributing

Contributions are welcome! Feel free to **fork this repository** and submit a **pull request**.

---

## 📩 Contact

For any questions, feel free to reach out:

**Email:** zaidchaudhrry@gmail.com  
**GitHub:** [zaidchaudhrry](https://github.com/zaidchaudhrry)
