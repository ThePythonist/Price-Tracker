import requests


def track_crypto_price(crypto_symbol):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_symbol}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()

    if crypto_symbol in data.keys():
        usd_price = data[crypto_symbol]['usd']
        toman_price = usd_price * 64700
        return toman_price
    else:
        return None


def main():
    crypto_symbol = input("Enter the cryptocurrency symbol: ")
    crypto_price = track_crypto_price(crypto_symbol)
    if crypto_price:
        # print(f"The current price of {crypto_symbol.upper()} is {crypto_price} Tomans")
        print(f"The current price of {crypto_symbol.upper()} is {int(crypto_price)} Tomans")
    else:
        print("Sorry, I couldn't fetch the cryptocurrency price at the moment. Please try again later.")


main()
