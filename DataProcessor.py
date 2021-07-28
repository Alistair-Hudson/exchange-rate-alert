import requests

url = 'https://api.exchangerate.host/latest'
response = requests.get(url, params={"base": "USD"})
data = response.json()


def RetrieveRates(currencies):
    rates = {}
    for currencey in currencies:
        rates[currencey] = data["rates"][currencey]

    return rates;
