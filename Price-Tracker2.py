from bs4 import BeautifulSoup
import requests


def get_price(symbol):
    urls = {
        "dollar": "https://www.tgju.org/profile/price_dollar_rl",
        "rob": "https://www.tgju.org/profile/rob",
        "nim": "https://www.tgju.org/profile/nim",
        "tamam": "https://www.tgju.org/profile/sekee",
    }
    url = urls[symbol]
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    spans = soup.find_all('span', class_='value')
    price = spans[0].text.split()[0]
    print(price)


get_price("nim")
