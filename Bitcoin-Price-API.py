import requests


def get_bitcoin_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()

    if 'bitcoin' in data.keys():
        return data['bitcoin']['usd']
    else:
        return None


bitcoin_price = get_bitcoin_price()
if bitcoin_price:
    print(f"The current price of Bitcoin is ${bitcoin_price}")
else:
    print("Sorry, I couldn't fetch the Bitcoin price at the moment. Please try again later.")
