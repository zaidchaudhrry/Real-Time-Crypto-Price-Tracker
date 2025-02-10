import streamlit as st
import requests
import pandas as pd
import time

# API URL
API_URL = "http://localhost:8000/latest-prices"

# Set page title
st.set_page_config(page_title="Real-Time Crypto Price Tracker", layout="wide")

st.title("📊 Real-Time Crypto Price Tracker")

# Function to fetch latest prices
def get_crypto_prices():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return []

# Initialize session state for price history
if "price_history" not in st.session_state:
    st.session_state.price_history = pd.DataFrame(columns=["currency", "price_usd", "timestamp"])

# Fetch new prices
crypto_data = get_crypto_prices()

if crypto_data:
    df = pd.DataFrame(crypto_data)
    
    # Convert timestamp to datetime format
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    # Append new data to session state
    st.session_state.price_history = pd.concat([st.session_state.price_history, df]).drop_duplicates().reset_index(drop=True)

    # Display the latest data
    st.subheader("📊 Latest Crypto Prices")
    st.dataframe(df)

    # Plot historical prices
    st.subheader("📈 Price Trend Over Time")
    for currency in df["currency"].unique():
        subset = st.session_state.price_history[st.session_state.price_history["currency"] == currency]
        st.line_chart(subset.set_index("timestamp")["price_usd"])

# Auto-refresh every 30 seconds
time.sleep(30)
st.rerun()

