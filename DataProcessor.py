import requests
import pymongo
import time


url = 'https://api.exchangerate.host/latest'

#Class for connecting to MongoDB
class Connect(object):
    @staticmethod
    def GetConnection():
        return pymongo.MongoClient("mongodb+srv://CurrencyX:CurrencyX@cluster0.mcbqk.mongodb.net/CurrencyX?retryWrites=true&w=majority")

#Retrieve exchange rates based on the USD
def RetrieveRates(currencies):
    response = requests.get(url, params={"base": "USD"})
    data = response.json()
    rates = {}
    currentTime = time.localtime(time.time())
    rates["currentTime"] = time.asctime(currentTime)
    for currencey in currencies:
        rates[currencey] = data["rates"][currencey]

    return rates;

#Store the Exchange rate data to MongoDB
def StoreRates(rates):
    connection =  Connect.GetConnection()
    db = connection.test
    db.currency.insert_one(rates)
    CheckAndRemoveOutofDateData(db)

#Limit the size of the database
def CheckAndRemoveOutofDateData(db):
    items = db.currency.find({})
    count = 0
    for item in items:
        count += 1
    if 5 < count:
        db.currency.delete_one({})

#Clear data base of all information
def ClearData():
    connection =  Connect.GetConnection()
    db = connection.test
    db.currency.delete_many({})
