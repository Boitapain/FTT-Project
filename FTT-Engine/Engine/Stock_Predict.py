import numpy as np
import pandas as pd
import math
import sklearn.preprocessing
import matplotlib.pyplot as plt
import tensorflow as tf
import os
import glob

amddf = pd.read_csv("Stock/stk_AMD.csv", index_col=0)
#print(amddf)

appledf = pd.read_csv("Stock/stk_Apple.csv", index_col=0)
#print(appledf)

gmedf = pd.read_csv("Stock/stk_Gamestop.csv", index_col=0)
#print(gmedf)

tesladf = pd.read_csv("Stock/stk_Tesla.csv", index_col=0)
#print(tesladf)

twitterdf = pd.read_csv("Stock/stk_Twitter.csv", index_col=0)
#print(twitterdf)

all_stk = os.path.join("Stock/","stk_*.csv")
all_stk = glob.glob(all_stk)
df = pd.concat(map(pd.read_csv, all_stk), ignore_index=True)
#print(df.keys())
#list = list(set(df.Symbol))[:5]
#print(list)

def stock_Price_Pred():
    amddf['Date'] = pd.to_datetime(amddf.Date, infer_datetime_format=True)
    amddf.sort_values(by="Date", ascending=False, inplace=True)
    print(amddf[["Open","Close"]])
    amdDifference =amddf[0:1].Close.values -amddf[0:1].Open.values
    print(amddf[0:1].Close.values + " " + amdDifference)

    appledf['Date'] = pd.to_datetime(appledf.Date, infer_datetime_format=True)
    appledf.sort_values(by="Date", ascending=False, inplace=True)
    appleDifference =appledf[0:1].Close.values -appledf[0:1].Open.values
    print(appledf[0:1].Close.values + " " + appleDifference)

    gmedf['Date'] = pd.to_datetime(gmedf.Date, infer_datetime_format=True)
    gmedf.sort_values(by="Date", ascending=False, inplace=True)
    gmeDifference =gmedf[0:1].Close.values -gmedf[0:1].Open.values
    print(gmedf[0:1].Close.values + " " + gmeDifference)

    tesladf['Date'] = pd.to_datetime(tesladf.Date, infer_datetime_format=True)
    tesladf.sort_values(by="Date", ascending=False, inplace=True)
    teslaDifference = tesladf[0:1].Close.values -tesladf[0:1].Open.values
    print(tesladf[0:1].Close.values + " " + teslaDifference)

    twitterdf['Date'] = pd.to_datetime(twitterdf.Date, infer_datetime_format=True)
    twitterdf.sort_values(by="Date", ascending=False, inplace=True)
    twitterDifference = twitterdf[0:1].Close.values -twitterdf[0:1].Open.values
    print(twitterdf[0:1].Close.values + " " + twitterDifference)
