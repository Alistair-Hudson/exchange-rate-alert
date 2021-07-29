import threading
import time

import DataProcessor
import AlertMonitor
import AlertHandler

currencies = ["AUD", "GBP", "USD", "NZD", "ILS", "EUR"]
exitFlag = False
useMultiThreading = False
sem = threading.Semaphore(0)

#Class to run currency information retrieve and storing into MongoDB
class DataThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while not(exitFlag):
            time.sleep(1)
            rates = DataProcessor.RetrieveRates(currencies)
            DataProcessor.StoreRates(rates)
            sem.release()

#Class for alert handling thread
class AlertThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while not(exitFlag):
            sem.acquire()
            print("retrieving data")
            time.sleep(1)
            rates = AlertMonitor.RetrieveData()
            changesInRates = AlertMonitor.ExtractData(rates)
            alerts = AlertMonitor.PingAlertsFor(changesInRates)
            AlertHandler.SendAlertMessage(alerts)

#Clear MongoDB to ensure only the latest information is used
DataProcessor.ClearData()
if useMultiThreading:
#This is code to run the app on multiple threads
    try:
        dataThread = DataThread()
        alertThread = AlertThread()
        dataThread.start()
        alertThread.start()
        while not(exitFlag):
            if "Q" ==input("Type Q to exit:"):
                exitFlag = True
        dataThread.join()
        alertThread.join()
        print("Program terminated")

    except:
        print("Error: unable to start thread")
else:
#Non multithreaded app
    while True:
        time.sleep(1)
        print("Retriving latest currency rates")
        currencies = ["AUD", "GBP", "USD", "NZD", "ILS", "EUR"]
        rates = DataProcessor.RetrieveRates(currencies)
        DataProcessor.StoreRates(rates)
        print("Preparing alerts")
        retrtievedRates = AlertMonitor.RetrieveData()
        changesInRates = AlertMonitor.ExtractData(retrtievedRates)
        alerts = AlertMonitor.PingAlertsFor(changesInRates)
        AlertHandler.SendAlertMessage(alerts)
        print("Alerts sent out")
