from time import time
import requests
import pymongo
import json
import pika

url = "https://webhook.site/45386ce0-3a23-4051-830c-cff7c560de95"
host = "185.139.25.6"
id = "1ff72efd-36ac-45cb-858d-e53a642a4180"

#Class for connecting to MongoDB
class Connect(object):
    @staticmethod
    def GetConnection():
        return pymongo.MongoClient("mongodb+srv://CurrencyX:CurrencyX@cluster0.mcbqk.mongodb.net/CurrencyX?retryWrites=true&w=majority")

#Send out alerts for the required currencies
def SendAlertMessage(ch, method, properties, body):
    message = body.decode()
    ch.basic_ack(delivery_tag=method.delivery_tag)
    json = {"defualt_status": 200,
            "default_content": message + " has shifted more than 0.0005",
            "default_content_type" : "text/html",}

    headers = {"api-key" : "00000000-0000-0000-0000-000000000000"}

    r = requests.post(url, json= json, headers= headers)

print("Running Alert Handler")

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue="alert", durable=True)
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue="alert",
                        on_message_callback=SendAlertMessage)
channel.start_consuming()
# while True:
#     connection = Connect.GetConnection()
#     alertDB = db.alerts.find({})
#     alerts = alertDB[0]
#     for currency in alerts:
#         if not("_id" == currency) and True == alerts[currency]:
#             SendAlertMessage(currency)
#     db.alerts.delete_one({})
            