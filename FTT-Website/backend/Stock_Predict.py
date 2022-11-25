import numpy as np
import pandas as pd
import math
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
# import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, LSTM

#Stock Datasets and Dataframes
amd_data = pd.read_csv("Stock/stk_AMD.csv")
amddf = pd.DataFrame(amd_data)

apple_data = pd.read_csv("Stock/stk_Apple.csv")
appledf = pd.DataFrame(apple_data)

gme_data = pd.read_csv("Stock/stk_Gamestop.csv")
gmedf = pd.DataFrame(gme_data)

tesla_data = pd.read_csv("Stock/stk_Tesla.csv")
tesladf = pd.DataFrame(tesla_data)

twitter_data = pd.read_csv("Stock/stk_Twitter.csv")
twitterdf = pd.DataFrame(twitter_data)


#AMD Prediction Graph Setup
amd_g_data = amddf.filter(["Close"])
amddataset = amd_g_data.values
amd_training_data_len = math.ceil(len(amddataset)*.8)

amd_scaler = MinMaxScaler(feature_range = (0, 1))
amd_scaled_data = amd_scaler.fit_transform(amddataset)

amd_train_data = amd_scaled_data[0: amd_training_data_len, :]
amd_x_train = []
amd_y_train = []
for i in range(60,len(amd_train_data)):
    amd_x_train.append(amd_train_data[i-60:i,0])
    amd_y_train.append(amd_train_data[i,0])

amd_x_train, amd_y_train = np.array(amd_x_train), np.array(amd_y_train)
amd_x_train = np.reshape(amd_x_train, (amd_x_train.shape[0], amd_x_train.shape[1], 1))

amd_model = Sequential()
amd_model.add(LSTM(50, return_sequences=True, input_shape=(amd_x_train.shape[1], 1)))
amd_model.add(LSTM(50, return_sequences=False))
amd_model.add(Dense(25))
amd_model.add(Dense(1))

amd_model.compile(optimizer='adam', loss='mean_squared_error')
#amd_model.fit(amd_x_train, amd_y_train, batch_size=1, epochs=1)
amd_model.fit(amd_x_train, amd_y_train, batch_size=1, epochs=0)

amd_test_data=amd_scaled_data[amd_training_data_len-60:,:]
amd_x_test = []
amd_y_test = amddataset[amd_training_data_len:,:]
for i in range(60, len(amd_test_data)):
    amd_x_test.append(amd_test_data[i-60:i,0])

amd_x_test = np.array(amd_x_test)
amd_x_test = np.reshape(amd_x_test,(amd_x_test.shape[0],amd_x_test.shape[1],1))

amd_predictions = amd_model.predict(amd_x_test)
amd_predictions = amd_scaler.inverse_transform(amd_predictions)

amd_g_train = amd_g_data[:amd_training_data_len]
amd_g_valid = amd_g_data[amd_training_data_len:]
amd_g_valid['predictions'] = amd_predictions


#Apple Prediction Graph Setup
apple_g_data = appledf.filter(["Close"])
appledataset = apple_g_data.values
apple_training_data_len = math.ceil(len(appledataset) * .8)

apple_scaler = MinMaxScaler(feature_range=(0, 1))
apple_scaled_data = apple_scaler.fit_transform(appledataset)

apple_train_data = apple_scaled_data[0: apple_training_data_len, :]
apple_x_train = []
apple_y_train = []
for i in range(60, len(apple_train_data)):
    apple_x_train.append(apple_train_data[i - 60:i, 0])
    apple_y_train.append(apple_train_data[i, 0])

apple_x_train, apple_y_train = np.array(apple_x_train), np.array(apple_y_train)
apple_x_train = np.reshape(apple_x_train, (apple_x_train.shape[0], apple_x_train.shape[1], 1))

apple_model = Sequential()
apple_model.add(LSTM(50, return_sequences=True, input_shape=(apple_x_train.shape[1], 1)))
apple_model.add(LSTM(50, return_sequences=False))
apple_model.add(Dense(25))
apple_model.add(Dense(1))

apple_model.compile(optimizer='adam', loss='mean_squared_error')
#apple_model.fit(apple_x_train, apple_y_train, batch_size=1, epochs=1)
apple_model.fit(apple_x_train, apple_y_train, batch_size=1, epochs=0)

apple_test_data = apple_scaled_data[apple_training_data_len - 60:, :]
apple_x_test = []
apple_y_test = appledataset[apple_training_data_len:, :]
for i in range(60, len(apple_test_data)):
    apple_x_test.append(apple_test_data[i - 60:i, 0])

apple_x_test = np.array(apple_x_test)
apple_x_test = np.reshape(apple_x_test, (apple_x_test.shape[0], apple_x_test.shape[1], 1))

apple_predictions = apple_model.predict(apple_x_test)
apple_predictions = apple_scaler.inverse_transform(apple_predictions)

apple_g_train = apple_g_data[:apple_training_data_len]
apple_g_valid = apple_g_data[apple_training_data_len:]
apple_g_valid['predictions'] = apple_predictions



#GME Prediction Graph Setup
gme_g_data = gmedf.filter(["Close"])
gmedataset = gme_g_data.values
gme_training_data_len = math.ceil(len(gmedataset) * .8)

gme_scaler = MinMaxScaler(feature_range=(0, 1))
gme_scaled_data = gme_scaler.fit_transform(gmedataset)

gme_train_data = gme_scaled_data[0: gme_training_data_len, :]
gme_x_train = []
gme_y_train = []
for i in range(60, len(gme_train_data)):
    gme_x_train.append(gme_train_data[i - 60:i, 0])
    gme_y_train.append(gme_train_data[i, 0])

gme_x_train, gme_y_train = np.array(gme_x_train), np.array(gme_y_train)
gme_x_train = np.reshape(gme_x_train, (gme_x_train.shape[0], gme_x_train.shape[1], 1))

gme_model = Sequential()
gme_model.add(LSTM(50, return_sequences=True, input_shape=(gme_x_train.shape[1], 1)))
gme_model.add(LSTM(50, return_sequences=False))
gme_model.add(Dense(25))
gme_model.add(Dense(1))

gme_model.compile(optimizer='adam', loss='mean_squared_error')
#gme_model.fit(gme_x_train, gme_y_train, batch_size=1, epochs=1)
gme_model.fit(gme_x_train, gme_y_train, batch_size=1, epochs=0)

gme_test_data = gme_scaled_data[gme_training_data_len - 60:, :]
gme_x_test = []
gme_y_test = gmedataset[gme_training_data_len:, :]
for i in range(60, len(gme_test_data)):
    gme_x_test.append(gme_test_data[i - 60:i, 0])

gme_x_test = np.array(gme_x_test)
gme_x_test = np.reshape(gme_x_test, (gme_x_test.shape[0], gme_x_test.shape[1], 1))

gme_predictions = gme_model.predict(gme_x_test)
gme_predictions = gme_scaler.inverse_transform(gme_predictions)

gme_g_train = gme_g_data[:gme_training_data_len]
gme_g_valid = gme_g_data[gme_training_data_len:]
gme_g_valid['predictions'] = gme_predictions


#Tesla Prediction Graph Setup
Tesla_g_data = tesladf.filter(["Close"])
tesladataset = Tesla_g_data.values
tesla_training_data_len = math.ceil(len(tesladataset) * .8)

tesla_scaler = MinMaxScaler(feature_range=(0, 1))
tesla_scaled_data = tesla_scaler.fit_transform(tesladataset)

tesla_train_data = tesla_scaled_data[0: tesla_training_data_len, :]
tesla_x_train = []
tesla_y_train = []
for i in range(60, len(tesla_train_data)):
    tesla_x_train.append(tesla_train_data[i - 60:i, 0])
    tesla_y_train.append(tesla_train_data[i, 0])

tesla_x_train, tesla_y_train = np.array(tesla_x_train), np.array(tesla_y_train)
tesla_x_train = np.reshape(tesla_x_train, (tesla_x_train.shape[0], tesla_x_train.shape[1], 1))

tesla_model = Sequential()
tesla_model.add(LSTM(50, return_sequences=True, input_shape=(tesla_x_train.shape[1], 1)))
tesla_model.add(LSTM(50, return_sequences=False))
tesla_model.add(Dense(25))
tesla_model.add(Dense(1))

tesla_model.compile(optimizer='adam', loss='mean_squared_error')
#tesla_model.fit(tesla_x_train, tesla_y_train, batch_size=1, epochs=1)
tesla_model.fit(tesla_x_train, tesla_y_train, batch_size=1, epochs=0)

tesla_test_data = tesla_scaled_data[tesla_training_data_len - 60:, :]
tesla_x_test = []
tesla_y_test = tesladataset[tesla_training_data_len:, :]
for i in range(60, len(tesla_test_data)):
    tesla_x_test.append(tesla_test_data[i - 60:i, 0])

tesla_x_test = np.array(tesla_x_test)
tesla_x_test = np.reshape(tesla_x_test, (tesla_x_test.shape[0], tesla_x_test.shape[1], 1))

tesla_predictions = tesla_model.predict(tesla_x_test)
tesla_predictions = tesla_scaler.inverse_transform(tesla_predictions)

tesla_g_train = Tesla_g_data[:tesla_training_data_len]
tesla_g_valid = Tesla_g_data[tesla_training_data_len:]
tesla_g_valid['predictions'] = tesla_predictions


#Twitter Prediction Graph Setup
twitter_g_data = twitterdf.filter(["Close"])
twitterdataset = twitter_g_data.values
twitter_training_data_len = math.ceil(len(twitterdataset) * .8)

twitter_scaler = MinMaxScaler(feature_range=(0, 1))
twitter_scaled_data = twitter_scaler.fit_transform(twitterdataset)

twitter_train_data = twitter_scaled_data[0: twitter_training_data_len, :]
twitter_x_train = []
twitter_y_train = []
for i in range(60, len(twitter_train_data)):
    twitter_x_train.append(twitter_train_data[i - 60:i, 0])
    twitter_y_train.append(twitter_train_data[i, 0])

twitter_x_train, twitter_y_train = np.array(twitter_x_train), np.array(twitter_y_train)
twitter_x_train = np.reshape(twitter_x_train, (twitter_x_train.shape[0], twitter_x_train.shape[1], 1))

twitter_model = Sequential()
twitter_model.add(LSTM(50, return_sequences=True, input_shape=(twitter_x_train.shape[1], 1)))
twitter_model.add(LSTM(50, return_sequences=False))
twitter_model.add(Dense(25))
twitter_model.add(Dense(1))

twitter_model.compile(optimizer='adam', loss='mean_squared_error')
#twitter_model.fit(twitter_x_train, twitter_y_train, batch_size=1, epochs=1)
twitter_model.fit(twitter_x_train, twitter_y_train, batch_size=1, epochs=0)

twitter_test_data = twitter_scaled_data[twitter_training_data_len - 60:, :]
twitter_x_test = []
twitter_y_test = twitterdataset[twitter_training_data_len:, :]
for i in range(60, len(twitter_test_data)):
    twitter_x_test.append(twitter_test_data[i - 60:i, 0])

twitter_x_test = np.array(twitter_x_test)
twitter_x_test = np.reshape(twitter_x_test, (twitter_x_test.shape[0], twitter_x_test.shape[1], 1))

twitter_predictions = twitter_model.predict(twitter_x_test)
twitter_predictions = twitter_scaler.inverse_transform(twitter_predictions)

twitter_g_train = twitter_g_data[:twitter_training_data_len]
twitter_g_valid = twitter_g_data[twitter_training_data_len:]
twitter_g_valid['predictions'] = twitter_predictions

def stock_Price_Pred(stock):

    if (stock == "amd"):
        amd_data['Date'] = pd.to_datetime(amd_data.Date, infer_datetime_format=True)
        amd_data.sort_values(by="Date", ascending=False, inplace=True)
        print(amd_data[["Open", "Close"]])
        amdDifference = amd_data[0:1].Close.values - amd_data[0:1].Open.values
#        print(amd_data[0:1].Close.values, " ", amdDifference)
        return amd_data[0:1].Close.values, " ", amdDifference

    elif (stock == "apple"):
        apple_data['Date'] = pd.to_datetime(apple_data.Date, infer_datetime_format=True)
        apple_data.sort_values(by="Date", ascending=False, inplace=True)
        appleDifference =apple_data[0:1].Close.values -apple_data[0:1].Open.values
#        print(apple_data[0:1].Close.values, " ", appleDifference)
        return apple_data[0:1].Close.values, " ", appleDifference

    elif (stock == "gme"):
        gme_data['Date'] = pd.to_datetime(gme_data.Date, infer_datetime_format=True)
        gme_data.sort_values(by="Date", ascending=False, inplace=True)
        gmeDifference =gme_data[0:1].Close.values -gme_data[0:1].Open.values
#        print(gmedf[0:1].Close.values, " ", gmeDifference)
        return gme_data[0:1].Close.values, " ", gmeDifference

    elif (stock == "tesla"):
        tesla_data['Date'] = pd.to_datetime(tesla_data.Date, infer_datetime_format=True)
        tesla_data.sort_values(by="Date", ascending=False, inplace=True)
        teslaDifference = tesla_data[0:1].Close.values - tesla_data[0:1].Open.values
#        print(tesladf[0:1].Close.values, " ", teslaDifference)
        return tesla_data[0:1].Close.values, " ", teslaDifference

    elif (stock == "twitter"):
        twitter_data['Date'] = pd.to_datetime(twitter_data.Date, infer_datetime_format=True)
        twitter_data.sort_values(by="Date", ascending=False, inplace=True)
        twitterDifference = twitter_data[0:1].Close.values -twitter_data[0:1].Open.values
#        print(twitterdf[0:1].Close.values, " ", twitterDifference)
        return twitter_data[0:1].Close.values, " ", twitterDifference

def graph_Stock_Predict(stock):

    if (stock == "amd"):
        plt.figure(figsize=(15, 5))
        plt.title('AMD Prediction')
        plt.xlabel('Date', fontsize=18)
        plt.ylabel('Close price', fontsize=18)
        plt.plot(amd_g_train['Close'])
        plt.plot(amd_g_valid['predictions'])
        plt.legend(['History','Prediction'], loc='best')
        return plt.show()

    elif (stock == "apple"):
        plt.figure(figsize=(15, 5))
        plt.title('Apple Prediction')
        plt.xlabel('Date', fontsize=18)
        plt.ylabel('Close price', fontsize=18)
        plt.plot(apple_g_train['Close'])
        plt.plot(apple_g_valid['predictions'])
        plt.legend(['History','Prediction'], loc='best')
        return plt.show()



    elif (stock == "gme"):
        plt.figure(figsize=(15, 5))
        plt.title('GME Prediction')
        plt.xlabel('Date', fontsize=18)
        plt.ylabel('Close price', fontsize=18)
        plt.plot(gme_g_train['Close'])
        plt.plot(gme_g_valid['predictions'])
        plt.legend(['History','Prediction'], loc='best')
        return plt.show()


    elif (stock == "tesla"):
        plt.figure(figsize=(15, 5))
        plt.title('Tesla Prediction')
        plt.xlabel('Date', fontsize=18)
        plt.ylabel('Close price', fontsize=18)
        plt.plot(tesla_g_train['Close'])
        plt.plot(tesla_g_valid['predictions'])
        plt.legend(['History','Prediction'], loc='best')
        return plt.show()

    elif (stock == "twitter"):
        plt.figure(figsize=(15, 5))
        plt.title('Twitter Prediction')
        plt.xlabel('Date', fontsize=18)
        plt.ylabel('Close price', fontsize=18)
        plt.plot(twitter_g_train['Close'])
        plt.plot(twitter_g_valid['predictions'])
        plt.legend(['History','Prediction'], loc='best')
        return plt.show()

def graph_Stock_Graph(stock):

    if (stock == "amd"):
        plt.figure(figsize=(15, 5))
        plt.title("AMD Close History")
        plt.plot(amddf['Close'])
        plt.xlabel('Date', fontsize=18)
        plt.ylabel('Close Price')
        return plt.show()

    elif (stock == "apple"):
        plt.figure(figsize=(15, 5))
        plt.title("Apple Close History")
        plt.plot(appledf["Close"])
        plt.xlabel("Date", fontsize=10)
        plt.ylabel("Close Price", fontsize=10)
        return plt.show()

    elif (stock == "gme"):
        plt.figure(figsize=(15, 5))
        plt.title("GME Close History")
        plt.plot(gmedf["Close"])
        plt.xlabel("Date", fontsize=10)
        plt.ylabel("Close Price", fontsize=10)
        return plt.show()

    elif (stock == "tesla"):
        plt.figure(figsize=(15, 5))
        plt.title("Tesla Close History")
        plt.plot(tesladf["Close"])
        plt.xlabel("Date", fontsize=10)
        plt.ylabel("Close Price", fontsize=10)
        return plt.show()

    elif (stock == "twitter"):
        plt.figure(figsize=(15, 5))
        plt.title("Twitter Close History")
        plt.plot(twitterdf["Close"])
        plt.xlabel("Date", fontsize=10)
        plt.ylabel("Close Price", fontsize=10)
        return plt.show()


"""
graph_Stock_Graph("amd")
graph_Stock_Predict("amd")

graph_Stock_Graph("apple")
graph_Stock_Predict("apple")

graph_Stock_Graph("twitter")
graph_Stock_Predict("twitter")

graph_Stock_Graph("gme")
graph_Stock_Predict("gme")

graph_Stock_Graph("tesla")
graph_Stock_Predict("tesla")
"""