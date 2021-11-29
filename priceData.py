from pycoingecko import CoinGeckoAPI
import numpy as np
import requests
import pandas as pd
import json

cg = CoinGeckoAPI()
pApi = 'gvmfl1vyDKqYI6PHEtV4xPCfUmAEYSCu'

def priceDataCG(coins, sDay, sMonth, sYear):
    days = 1
    prices = []
    dates = []
    for coin in range(0,len(coins)):
        tmpPrices = []
        tmpDates = []
        print(coins[coin])
        for i in range(0,1):
            date = str(sDay+i)+'-'+str(sMonth)+'-'+str(sYear)
            x = requests.get('https://api.coingecko.com/api/v3/coins/'+coins[coin]+'/history?date=' +date+'&localization=usd' + '?format=json' )
            check = x.json()
            price = check["market_data"]["current_price"]['usd']
            #priceDict[date] = price

            tmpPrices.append(price)
            tmpDates.append(date)

        prices.append(tmpPrices)
        dates.append(tmpDates)
        #print(priceDict)
        #coinPrices.append(priceDict)
        
    print(prices)
    print(dates)

def priceDataPoly(coins, sDay, sMonth, sYear):
    
    for i in range(0,1):
        if(sDay > 9):
            date = str(sYear)+'-'+str(sMonth)+'-'+str(sDay)
        else:
            date = str(sYear)+'-'+str(sMonth)+'-'+'0'+ str(sDay)
        x = requests.get('https://api.polygon.io/v1/open-close/crypto/ETH/USD/'+date+'?adjusted=false&apiKey='+pApi)
        check = x.json()
        print(check["day"])
        print(check["close"])

def main():
    coins = ['joe', 'bitcoin']
    sDay = 1
    sMonth = 11
    sYear = 2021
    priceDataCG(coins, sDay, sMonth, sYear)

main()
