import numpy as np
import pandas as pd
import math
import sklearn.preprocessing
import matplotlib.pyplot as plt
import tensorflow as tf
import os
import glob

valid_percentage = 10
test_percentage = 10

binanceCoindf = pd.read_csv("Crypto/coin_BinanceCoin.csv", index_col=0)
#binanceCoindf.info()
#print(binanceCoindf.head())

bitcoindf = pd.read_csv("Crypto/coin_Bitcoin.csv", index_col=0)
#bitcoindf.info()
#print(bitcoindf.head())

cardanodf = pd.read_csv("Crypto/coin_Cardano.csv", index_col=0)
#cardanodf.info()
#print(cardanodf.head())

dogecoindf = pd.read_csv("Crypto/coin_Dogecoin.csv", index_col=0)
#dogecoindf.info()
#print(dogecoindf.head())

ethereumdf = pd.read_csv("Crypto/coin_Ethereum.csv", index_col=0)
#ethereumdf.info()
#print(ethereumdf.head())

all_coins = os.path.join("Crypto/","coin_*.csv")
all_coins = glob.glob(all_coins)
df = pd.concat(map(pd.read_csv, all_coins), ignore_index=True)
#print(df)

list = list(set(df.Symbol))[:5]
#['ADA', 'DOGE', 'BTC', 'ETH', 'BNB']
#df.info()

def crypto_Price_Diff():
    binanceCoindf['Date'] = pd.to_datetime(binanceCoindf.Date, infer_datetime_format=True)
    #print(df.head())
    binanceCoindf.sort_values(by="Date", ascending=False, inplace=True)
    print(binanceCoindf[["Open","Close"]])
    #Binance Coin  302.195584  320.934802
    binanceDifference =binanceCoindf[0:1].Close.values -binanceCoindf[0:1].Open.values
    return(binanceCoindf[0:1].Close.values + " " + binanceDifference)
    #[18.7392174]

    bitcoindf['Date'] = pd.to_datetime(bitcoindf.Date, infer_datetime_format=True)
    bitcoindf.sort_values(by="Date", ascending=False, inplace=True)
    bitcoinDifference =bitcoindf[0:1].Close.values -bitcoindf[0:1].Open.values
    return(bitcoindf[0:1].Close.values + " " + bitcoinDifference)

    cardanodf['Date'] = pd.to_datetime(cardanodf.Date, infer_datetime_format=True)
    cardanodf.sort_values(by="Date", ascending=False, inplace=True)
    cardanoDifference =cardanodf[0:1].Close.values -cardanodf[0:1].Open.values
    return(cardanodf[0:1].Close.values + " " + cardanoDifference)

    dogecoindf['Date'] = pd.to_datetime(dogecoindf.Date, infer_datetime_format=True)
    dogecoindf.sort_values(by="Date", ascending=False, inplace=True)
    dogecoinDifference =dogecoindf[0:1].Close.values -dogecoindf[0:1].Open.values
    return(dogecoindf[0:1].Close.values + " " + dogecoinDifference)

    ethereumdf['Date'] = pd.to_datetime(ethereumdf.Date, infer_datetime_format=True)
    ethereumdf.sort_values(by="Date", ascending=False, inplace=True)
    ethereumDifference =ethereumdf[0:1].Close.values -ethereumdf[0:1].Open.values
    return(ethereumdf[0:1].Close.values + " " + ethereumDifference)


