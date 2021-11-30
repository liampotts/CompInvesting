from pycoingecko import CoinGeckoAPI
import numpy as np
import requests
import pandas as pd
import json

cg = CoinGeckoAPI()
pApi = 'gvmfl1vyDKqYI6PHEtV4xPCfUmAEYSCu'



def priceDataCG(coins, sDay, sMonth, sYear, days):
    df = pd.DataFrame(columns = ['Date',coins[0]])
    for coin in range(0,1):
        for i in range(0,days):
            date = str(sDay+i)+'-'+str(sMonth)+'-'+str(sYear)
            x = requests.get('https://api.coingecko.com/api/v3/coins/'+coins[coin]+'/history?date=' +date+'&localization=usd' + '?format=json' )
            check = x.json()
            price = check["market_data"]["current_price"]['usd']
            df = df.append({'Date' : date, coins[0]:price},
                            ignore_index = True)
    return df
        

def main():
    coins = ['joe', 'bitcoin']
    sDay = 1
    sMonth = 11
    sYear = 2021
    days = 5
    print (priceDataCG(coins, sDay, sMonth, sYear, days))

main()
