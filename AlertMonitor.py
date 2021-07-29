import pymongo

#Class for connecting to MongoDB
class Connect(object):
    @staticmethod
    def GetConnection():
        return pymongo.MongoClient("mongodb+srv://CurrencyX:CurrencyX@cluster0.mcbqk.mongodb.net/CurrencyX?retryWrites=true&w=majority")

#Retrieve database from MongoDB
def RetrieveData():
    connection = Connect.GetConnection()
    db = connection.test
    rates = db.currency.find({})
    db.currency.delete_one({})
    return rates

#Extract the required data and compare
def ExtractData(rates):
    try:
        previousRates = rates[0]
        currentRates = rates[1]
        changesInRates = {}
        for currencey in previousRates:
            if not("_id" == currencey or "currentTime" == currencey):
                changesInRates[currencey] = currentRates[currencey] - previousRates[currencey]
        return changesInRates
    except:
        print("Not enough data")
        return []

#Set which currencices are to be alerted for
def PingAlertsFor(changesInRates):
    alerts = {}
    for currency in changesInRates:
        if 0.0005 <= changesInRates[currency] or -0.0005 >= changesInRates[currency]:
            alerts[currency] = True
        else:
            alerts[currency] = False
    return alerts

