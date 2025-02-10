import requests
import json

# Define the API URL
API_URL = "https://api.coingecko.com/api/v3/simple/price"

# Define query parameters
params = {
    "ids": "bitcoin,ethereum,cardano",
    "vs_currencies": "usd"
}

def fetch_crypto_prices():
    """Fetch real-time crypto prices from CoinGecko API."""
    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()  # Raise an error if the request fails
        data = response.json()
        print("Fetched Data from API:", data)  # Debugging
        return data
    except requests.exceptions.RequestException as e:
        print("❌ Error fetching data:", e)
        return None

# Test the function
if __name__ == "__main__":
    prices = fetch_crypto_prices()
    print(json.dumps(prices, indent=2))  # Pretty print the response
