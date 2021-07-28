import threading
import time

import DataProcessor

def ProcessCurrencies():

    while True:
        time.sleep(1)
        currencies = ["AUD", "GBP", "USD", "NZD", "ILS", "EUR"]
        rates = DataProcessor.RetrieveRates(currencies)
        DataProcessor.StoreRates(rates)


try:
    threading.start_new_thread(ProcessCurrencies)
except:
    print("Error: unable to start thread")