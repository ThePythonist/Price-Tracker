import requests

def get_crypto_price(crypto_id, currency):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies={currency}"
    response = requests.get(url)
    data = response.json()
    crypto_price = data[crypto_id][currency]
    return crypto_price

# Example usage
crypto_id = "tether"
currency = "usd"
crypto_price = get_crypto_price(crypto_id, currency)
print(f"The current price of {crypto_id.capitalize()} is ${crypto_price}")
