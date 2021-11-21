from pycoingecko import CoinGeckoAPI
import numpy as np
import requests
cg = CoinGeckoAPI()

def priceData(coins, sDay, sMonth, sYear):
    
    for i in range(0,1):
        date = str(sDay+i)+'-'+str(sMonth)+'-'+str(sYear)
        x = requests.get('https://api.coingecko.com/api/v3/coins/joe/history?date=' +date+'&localization=usd'+ '?format=json')
        print(x)

def main():
    coins = ['joe']
    sDay = 1
    sMonth = 11
    sYear = 2021
    priceData(coins, sDay, sMonth, sYear)

main()
