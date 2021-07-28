import DataProcessor

def RetrieveData():
    connection = DataProcessor.Connect.GetConnection()
    db = connection.test
    rates = db.currency.find({})
    return rates

def ExtractData(rates):
    previousRates = rates[0]
    currentRates = rates[1]
    changesInRates = {}
    for currencey in previousRates:
        if not("_id" == currencey or "currentTime" == currencey):
            changesInRates[currencey] = currentRates[currencey] - previousRates[currencey]
    return changesInRates

def PingAlertsFor(changesInRates):
    alerts = {}
    for currency in changesInRates:
        if 0.0005 <= changesInRates[currency] or -0.0005 >= changesInRates[currency]:
            alerts[currency] = True
        else:
            alerts[currency] = False
    return alerts


rates = RetrieveData()
changesInRates = ExtractData(rates)
print(PingAlertsFor(changesInRates))