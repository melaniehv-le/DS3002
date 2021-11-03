#Quiz 2

import json
import requests
import time
import csv

apikey='UERf5Pj6w99i7k25hBgN9w5JWhLDKfs1z09PYmmb'
work = False
while(work==False):
    url = "https://yfapi.net/v6/finance/quote"
    ticker = input("Hello, please input ticker: ")

    querystring = {"symbols":ticker}
    headers = {
      'x-api-key': apikey
       }
    response = requests.request("GET", url, headers=headers, params=querystring)
    #print(response.text)

    response.raise_for_status()  # raises exception when not a 2xx response
    #if response.status_code != 204:
    stock_json = response.json()
    #print(stock_json)
    #print(stock_json['quoteResponse']['result'][0]["displayName"] + " Price:$" + str(stock_json['quoteResponse']['result'][0]["regularMarketPrice"]))

    if len(stock_json['quoteResponse']['result']) == 0:
        print("Wrong ticker")
        work=0

    else:
        work=1

        timestamp = stock_json['quoteResponse']['result'][0]["regularMarketTime"]

        compname = stock_json['quoteResponse']['result'][0]["displayName"]
        marketp = stock_json['quoteResponse']['result'][0]["regularMarketPrice"]
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(timestamp))
        print(compname, date, marketp)


        with open('stock.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([ticker, date, marketp])


