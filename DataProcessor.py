import requests
import pymongo
import time


url = 'https://api.exchangerate.host/latest'
response = requests.get(url, params={"base": "USD"})
data = response.json()

class Connect(object):
    @staticmethod
    def GetConnection():
        return pymongo.MongoClient("mongodb+srv://CurrencyX:CurrencyX@cluster0.mcbqk.mongodb.net/CurrencyX?retryWrites=true&w=majority")


def RetrieveRates(currencies):
    rates = {}
    currentTime = time.localtime(time.time())
    rates["currentTime"] = time.asctime(currentTime)
    for currencey in currencies:
        rates[currencey] = data["rates"][currencey]

    return rates;

def StoreRates(rates):
    connection =  Connect.GetConnection()
    db = connection.test
    db.currency.insert_one(rates)
    CheckAndRemoveOutofDateData(db)

def CheckAndRemoveOutofDateData(db):
    items = db.currency.find({})
    count = 0
    for item in items:
        count += 1
    if 5 < count:
        db.currency.delete_one({})

def ClearData():
    connection =  Connect.GetConnection()
    db = connection.test
    db.currency.delete_many({})