import requests


def ping():
    url = "https://api.coingecko.com/api/v3/ping"
    assert requests.get(url).json()[
        "gecko_says"] == "(V3) To the Moon!", "API down"


def get_symbol(coin):
    url = f"https://api.coingecko.com/api/v3/coins/{coin}"
    return requests.get(url).json()["symbol"].upper()


def get_price(coin, currency):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies={currency}"
    return requests.get(url).json()[coin][currency]