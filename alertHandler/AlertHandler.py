import requests
import pymongo
import json


url = "https://webhook.site/45386ce0-3a23-4051-830c-cff7c560de95"
host = "185.139.25.6"
id = "1ff72efd-36ac-45cb-858d-e53a642a4180"


#Class for connecting to MongoDB
class Connect(object):
    @staticmethod
    def GetConnection():
        return pymongo.MongoClient("mongodb+srv://CurrencyX:CurrencyX@cluster0.mcbqk.mongodb.net/CurrencyX?retryWrites=true&w=majority")

#Send out alerts for the required currencies
def SendAlertMessage(currency):
    json = {"defualt_status": 200,
            "default_content": str(currency) + " has shifted more than 0.0005",
            "default_content_type" : "text/html",}

    headers = {"api-key" : "00000000-0000-0000-0000-000000000000"}

    r = requests.post(url, json= json, headers= headers)
    # print(r.json["uuid"])


print("Running Alert Handler")
while True:
    connection = Connect.GetConnection()
    db = connection.test
    alertDB = db.alerts.find({})
    alerts = alertDB[0]
    for currency in alerts:
        if not("_id" == currency) and True == alerts[currency]:
            SendAlertMessage(currency)
    db.alerts.delete_one({})
            