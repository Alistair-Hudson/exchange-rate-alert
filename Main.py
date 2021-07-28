from re import T
import threading
import time

import DataProcessor
import AlertMonitor
import AlertHandler

exitFlag = False
sem = threading.Semaphore(0)

class DataThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while not(exitFlag):
            time.sleep(1)
            currencies = ["AUD", "GBP", "USD", "NZD", "ILS", "EUR"]
            rates = DataProcessor.RetrieveRates(currencies)
            DataProcessor.StoreRates(rates)
            sem.release()
        DataProcessor.ClearData();

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
