import requests
import pymongo


url = 'https://api.exchangerate.host/latest'
response = requests.get(url, params={"base": "USD"})
data = response.json()

class Connect(object):
    @staticmethod
    def GetConnection():
        return pymongo.MongoClient("mongodb+srv://CurrencyX:CurrencyX@cluster0.mcbqk.mongodb.net/CurrencyX?retryWrites=true&w=majority")


def RetrieveRates(currencies):
    rates = {}
    for currencey in currencies:
        rates[currencey] = data["rates"][currencey]

    return rates;

def StoreRates(rates):
    connection =  Connect.GetConnection()
    db = connection.test
    db.currency.insert_one(rates)