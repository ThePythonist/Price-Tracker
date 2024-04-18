from bs4 import BeautifulSoup
import requests


def solution1():
    url = "https://www.tgju.org/profile/rob"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    elements = soup.find_all("span", class_="value")
    elements = str(elements[2]).split()
    print(elements[3].split(">")[1].split("<")[0])


def solution2():
    url = "https://www.tgju.org/profile/rob"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    spans = soup.find_all('span', class_='value')
    price = spans[0].text.split()[0]
    print(price)

solution2()
