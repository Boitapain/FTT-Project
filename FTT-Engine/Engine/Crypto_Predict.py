import numpy as np
import pandas as pd
import math
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, LSTM


#Crypto Datasets and Dataframes
binanceCoinData = pd.read_csv("Crypto/coin_BinanceCoin.csv")
binanceCoindf = pd.DataFrame(binanceCoinData)

bitcoinData = pd.read_csv("Crypto/coin_Bitcoin.csv")
bitcoindf = pd.DataFrame(bitcoinData)

cardanoData = pd.read_csv("Crypto/coin_Cardano.csv")
cardanodf = pd.DataFrame(cardanoData)

dogecoinData = pd.read_csv("Crypto/coin_Dogecoin.csv")
dogecoindf = pd.DataFrame(dogecoinData)

ethereumData = pd.read_csv("Crypto/coin_Ethereum.csv")
ethereumdf = pd.DataFrame(ethereumData)



#BinanceCoin Prediction Graph Setup
binanceCoin_g_data = binanceCoindf.filter(["Close"])
binanceCoindataset = binanceCoin_g_data.values
binanceCoin_training_data_len = math.ceil(len(binanceCoindataset)*.8)

binanceCoin_scaler = MinMaxScaler(feature_range = (0, 1))
binanceCoin_scaled_data = binanceCoin_scaler.fit_transform(binanceCoindataset)

binanceCoin_train_data = binanceCoin_scaled_data[0: binanceCoin_training_data_len, :]
binanceCoin_x_train = []
binanceCoin_y_train = []
for i in range(60,len(binanceCoin_train_data)):
    binanceCoin_x_train.append(binanceCoin_train_data[i-60:i,0])
    binanceCoin_y_train.append(binanceCoin_train_data[i,0])

binanceCoin_x_train, binanceCoin_y_train = np.array(binanceCoin_x_train), np.array(binanceCoin_y_train)
binanceCoin_x_train = np.reshape(binanceCoin_x_train, (binanceCoin_x_train.shape[0], binanceCoin_x_train.shape[1], 1))

binanceCoin_model = Sequential()
binanceCoin_model.add(LSTM(50, return_sequences=True, input_shape=(binanceCoin_x_train.shape[1], 1)))
binanceCoin_model.add(LSTM(50, return_sequences=False))
binanceCoin_model.add(Dense(25))
binanceCoin_model.add(Dense(1))

binanceCoin_model.compile(optimizer='adam', loss='mean_squared_error')
binanceCoin_model.fit(binanceCoin_x_train, binanceCoin_y_train, batch_size=1, epochs=1)

binanceCoin_test_data=binanceCoin_scaled_data[binanceCoin_training_data_len-60:,:]
binanceCoin_x_test = []
binanceCoin_y_test = binanceCoindataset[binanceCoin_training_data_len:,:]
for i in range(60, len(binanceCoin_test_data)):
    binanceCoin_x_test.append(binanceCoin_test_data[i-60:i,0])

binanceCoin_x_test = np.array(binanceCoin_x_test)
binanceCoin_x_test = np.reshape(binanceCoin_x_test,(binanceCoin_x_test.shape[0],binanceCoin_x_test.shape[1],1))

binanceCoin_predictions = binanceCoin_model.predict(binanceCoin_x_test)
binanceCoin_predictions = binanceCoin_scaler.inverse_transform(binanceCoin_predictions)

binanceCoin_g_train = binanceCoin_g_data[:binanceCoin_training_data_len]
binanceCoin_g_valid = binanceCoin_g_data[binanceCoin_training_data_len:]
binanceCoin_g_valid['predictions'] = binanceCoin_predictions


#Bitcoin Prediction Graph Setup
bitcoin_g_data = bitcoindf.filter(["Close"])
bitcoindataset = bitcoin_g_data.values
bitcoin_training_data_len = math.ceil(len(bitcoindataset)*.8)

bitcoin_scaler = MinMaxScaler(feature_range = (0, 1))
bitcoin_scaled_data = bitcoin_scaler.fit_transform(bitcoindataset)

bitcoin_train_data = bitcoin_scaled_data[0: bitcoin_training_data_len, :]
bitcoin_x_train = []
bitcoin_y_train = []
for i in range(60,len(bitcoin_train_data)):
    bitcoin_x_train.append(bitcoin_train_data[i-60:i,0])
    bitcoin_y_train.append(bitcoin_train_data[i,0])

bitcoin_x_train, bitcoin_y_train = np.array(bitcoin_x_train), np.array(bitcoin_y_train)
bitcoin_x_train = np.reshape(bitcoin_x_train, (bitcoin_x_train.shape[0], bitcoin_x_train.shape[1], 1))

bitcoin_model = Sequential()
bitcoin_model.add(LSTM(50, return_sequences=True, input_shape=(bitcoin_x_train.shape[1], 1)))
bitcoin_model.add(LSTM(50, return_sequences=False))
bitcoin_model.add(Dense(25))
bitcoin_model.add(Dense(1))

bitcoin_model.compile(optimizer='adam', loss='mean_squared_error')
bitcoin_model.fit(bitcoin_x_train, bitcoin_y_train, batch_size=1, epochs=1)

bitcoin_test_data=bitcoin_scaled_data[bitcoin_training_data_len-60:,:]
bitcoin_x_test = []
bitcoin_y_test = bitcoindataset[bitcoin_training_data_len:,:]
for i in range(60, len(bitcoin_test_data)):
    bitcoin_x_test.append(bitcoin_test_data[i-60:i,0])

bitcoin_x_test = np.array(bitcoin_x_test)
bitcoin_x_test = np.reshape(bitcoin_x_test,(bitcoin_x_test.shape[0],bitcoin_x_test.shape[1],1))

bitcoin_predictions = bitcoin_model.predict(bitcoin_x_test)
bitcoin_predictions = bitcoin_scaler.inverse_transform(bitcoin_predictions)

bitcoin_g_train = bitcoin_g_data[:bitcoin_training_data_len]
bitcoin_g_valid = bitcoin_g_data[bitcoin_training_data_len:]
bitcoin_g_valid['predictions'] = bitcoin_predictions




#Cardano Prediction Graph Setup
cardano_g_data = cardanodf.filter(["Close"])
cardanodataset = cardano_g_data.values
cardano_training_data_len = math.ceil(len(cardanodataset)*.8)

cardano_scaler = MinMaxScaler(feature_range = (0, 1))
cardano_scaled_data = cardano_scaler.fit_transform(cardanodataset)

cardano_train_data = cardano_scaled_data[0: cardano_training_data_len, :]
cardano_x_train = []
cardano_y_train = []
for i in range(60,len(cardano_train_data)):
    cardano_x_train.append(cardano_train_data[i-60:i,0])
    cardano_y_train.append(cardano_train_data[i,0])

cardano_x_train, cardano_y_train = np.array(cardano_x_train), np.array(cardano_y_train)
cardano_x_train = np.reshape(cardano_x_train, (cardano_x_train.shape[0], cardano_x_train.shape[1], 1))

cardano_model = Sequential()
cardano_model.add(LSTM(50, return_sequences=True, input_shape=(cardano_x_train.shape[1], 1)))
cardano_model.add(LSTM(50, return_sequences=False))
cardano_model.add(Dense(25))
cardano_model.add(Dense(1))

cardano_model.compile(optimizer='adam', loss='mean_squared_error')
cardano_model.fit(cardano_x_train, cardano_y_train, batch_size=1, epochs=1)

cardano_test_data=cardano_scaled_data[cardano_training_data_len-60:,:]
cardano_x_test = []
cardano_y_test = cardanodataset[cardano_training_data_len:,:]
for i in range(60, len(cardano_test_data)):
    cardano_x_test.append(cardano_test_data[i-60:i,0])

cardano_x_test = np.array(cardano_x_test)
cardano_x_test = np.reshape(cardano_x_test,(cardano_x_test.shape[0],cardano_x_test.shape[1],1))

cardano_predictions = cardano_model.predict(cardano_x_test)
cardano_predictions = cardano_scaler.inverse_transform(cardano_predictions)

cardano_g_train = cardano_g_data[:cardano_training_data_len]
cardano_g_valid = cardano_g_data[cardano_training_data_len:]
cardano_g_valid['predictions'] = cardano_predictions



#Dogecoin Prediction Graph Setup
dogecoin_g_data = dogecoindf.filter(["Close"])
dogecoindataset = dogecoin_g_data.values
dogecoin_training_data_len = math.ceil(len(dogecoindataset)*.8)

dogecoin_scaler = MinMaxScaler(feature_range = (0, 1))
dogecoin_scaled_data = dogecoin_scaler.fit_transform(dogecoindataset)

dogecoin_train_data = dogecoin_scaled_data[0: dogecoin_training_data_len, :]
dogecoin_x_train = []
dogecoin_y_train = []
for i in range(60,len(dogecoin_train_data)):
    dogecoin_x_train.append(dogecoin_train_data[i-60:i,0])
    dogecoin_y_train.append(dogecoin_train_data[i,0])

dogecoin_x_train, dogecoin_y_train = np.array(dogecoin_x_train), np.array(dogecoin_y_train)
dogecoin_x_train = np.reshape(dogecoin_x_train, (dogecoin_x_train.shape[0], dogecoin_x_train.shape[1], 1))

dogecoin_model = Sequential()
dogecoin_model.add(LSTM(50, return_sequences=True, input_shape=(dogecoin_x_train.shape[1], 1)))
dogecoin_model.add(LSTM(50, return_sequences=False))
dogecoin_model.add(Dense(25))
dogecoin_model.add(Dense(1))

dogecoin_model.compile(optimizer='adam', loss='mean_squared_error')
dogecoin_model.fit(dogecoin_x_train, dogecoin_y_train, batch_size=1, epochs=1)

dogecoin_test_data=dogecoin_scaled_data[dogecoin_training_data_len-60:,:]
dogecoin_x_test = []
dogecoin_y_test = dogecoindataset[dogecoin_training_data_len:,:]
for i in range(60, len(dogecoin_test_data)):
    dogecoin_x_test.append(dogecoin_test_data[i-60:i,0])

dogecoin_x_test = np.array(dogecoin_x_test)
dogecoin_x_test = np.reshape(dogecoin_x_test,(dogecoin_x_test.shape[0],dogecoin_x_test.shape[1],1))

dogecoin_predictions = dogecoin_model.predict(dogecoin_x_test)
dogecoin_predictions = dogecoin_scaler.inverse_transform(dogecoin_predictions)

dogecoin_g_train = dogecoin_g_data[:dogecoin_training_data_len]
dogecoin_g_valid = dogecoin_g_data[dogecoin_training_data_len:]
dogecoin_g_valid['predictions'] = dogecoin_predictions




#Ethereum Prediction Graph Setup
ethereum_g_data = ethereumdf.filter(["Close"])
ethereumdataset = ethereum_g_data.values
ethereum_training_data_len = math.ceil(len(ethereumdataset)*.8)

ethereum_scaler = MinMaxScaler(feature_range = (0, 1))
ethereum_scaled_data = ethereum_scaler.fit_transform(ethereumdataset)

ethereum_train_data = ethereum_scaled_data[0: ethereum_training_data_len, :]
ethereum_x_train = []
ethereum_y_train = []
for i in range(60,len(ethereum_train_data)):
    ethereum_x_train.append(ethereum_train_data[i-60:i,0])
    ethereum_y_train.append(ethereum_train_data[i,0])

ethereum_x_train, ethereum_y_train = np.array(ethereum_x_train), np.array(ethereum_y_train)
ethereum_x_train = np.reshape(ethereum_x_train, (ethereum_x_train.shape[0], ethereum_x_train.shape[1], 1))

ethereum_model = Sequential()
ethereum_model.add(LSTM(50, return_sequences=True, input_shape=(ethereum_x_train.shape[1], 1)))
ethereum_model.add(LSTM(50, return_sequences=False))
ethereum_model.add(Dense(25))
ethereum_model.add(Dense(1))

ethereum_model.compile(optimizer='adam', loss='mean_squared_error')
ethereum_model.fit(ethereum_x_train, ethereum_y_train, batch_size=1, epochs=1)

ethereum_test_data=ethereum_scaled_data[ethereum_training_data_len-60:,:]
ethereum_x_test = []
ethereum_y_test = ethereumdataset[ethereum_training_data_len:,:]
for i in range(60, len(ethereum_test_data)):
    ethereum_x_test.append(ethereum_test_data[i-60:i,0])

ethereum_x_test = np.array(ethereum_x_test)
ethereum_x_test = np.reshape(ethereum_x_test,(ethereum_x_test.shape[0],ethereum_x_test.shape[1],1))

ethereum_predictions = ethereum_model.predict(ethereum_x_test)
ethereum_predictions = ethereum_scaler.inverse_transform(ethereum_predictions)

ethereum_g_train = ethereum_g_data[:ethereum_training_data_len]
ethereum_g_valid = ethereum_g_data[ethereum_training_data_len:]
ethereum_g_valid['predictions'] = ethereum_predictions


def crypto_Price_Diff():
    binanceCoinData['Date'] = pd.to_datetime(binanceCoinData.Date, infer_datetime_format=True)
    #print(df.head())
    binanceCoinData.sort_values(by="Date", ascending=False, inplace=True)
    print(binanceCoinData[["Open","Close"]])
    #Binance Coin  302.195584  320.934802
    binanceDifference =binanceCoinData[0:1].Close.values -binanceCoinData[0:1].Open.values
    return(binanceCoinData[0:1].Close.values, " ", binanceDifference)
    #[18.7392174]

    bitcoinData['Date'] = pd.to_datetime(bitcoinData.Date, infer_datetime_format=True)
    bitcoinData.sort_values(by="Date", ascending=False, inplace=True)
    bitcoinDifference =bitcoinData[0:1].Close.values -bitcoinData[0:1].Open.values
    return(bitcoinData[0:1].Close.values, " ", bitcoinDifference)

    cardanoData['Date'] = pd.to_datetime(cardanoData.Date, infer_datetime_format=True)
    cardanoData.sort_values(by="Date", ascending=False, inplace=True)
    cardanoDifference =cardanoData[0:1].Close.values -cardanoData[0:1].Open.values
    return(cardanoData[0:1].Close.values, " ", cardanoDifference)

    dogecoinData['Date'] = pd.to_datetime(dogecoinData.Date, infer_datetime_format=True)
    dogecoinData.sort_values(by="Date", ascending=False, inplace=True)
    dogecoinDifference =dogecoinData[0:1].Close.values -dogecoinData[0:1].Open.values
    return(dogecoinData[0:1].Close.values, " ", dogecoinDifference)

    ethereumData['Date'] = pd.to_datetime(ethereumData.Date, infer_datetime_format=True)
    ethereumData.sort_values(by="Date", ascending=False, inplace=True)
    ethereumDifference =ethereumData[0:1].Close.values -ethereumData[0:1].Open.values
    return(ethereumData[0:1].Close.values, " ", ethereumDifference)


def graph_Stock_Predict(stock):

    if (stock == "binance"):
        plt.figure(figsize=(15, 5))
        plt.title('Binance Prediction')
        plt.xlabel('Date', fontsize=18)
        plt.ylabel('Close price', fontsize=18)
        plt.plot(binanceCoin_g_train['Close'])
        plt.plot(binanceCoin_g_valid[['Close', 'predictions']])
        plt.legend(['History', 'Valid', 'Prediction'], loc='lower right')
        plt.show()

    elif (stock == "bitcoin"):
        plt.figure(figsize=(15, 5))
        plt.title('Bitcoin Prediction')
        plt.xlabel('Date', fontsize=18)
        plt.ylabel('Close price', fontsize=18)
        plt.plot(bitcoin_g_train['Close'])
        plt.plot(bitcoin_g_valid[['Close', 'predictions']])
        plt.legend(['History', 'Valid', 'Prediction'], loc='lower right')
        plt.show()



    elif (stock == "cardano"):
        plt.figure(figsize=(15, 5))
        plt.title('Cardano Prediction')
        plt.xlabel('Date', fontsize=18)
        plt.ylabel('Close price', fontsize=18)
        plt.plot(cardano_g_train['Close'])
        plt.plot(cardano_g_valid[['Close', 'predictions']])
        plt.legend(['History', 'Valid', 'Prediction'], loc='lower right')
        plt.show()


    elif (stock == "dogecoin"):
        plt.figure(figsize=(15, 5))
        plt.title('Dogecoin Prediction')
        plt.xlabel('Date', fontsize=18)
        plt.ylabel('Close price', fontsize=18)
        plt.plot(dogecoin_g_train['Close'])
        plt.plot(dogecoin_g_valid[['Close', 'predictions']])
        plt.legend(['History', 'Valid', 'Prediction'], loc='lower right')
        plt.show()

    elif (stock == "Ethereum"):
        plt.figure(figsize=(15, 5))
        plt.title('Ethereum Prediction')
        plt.xlabel('Date', fontsize=18)
        plt.ylabel('Close price', fontsize=18)
        plt.plot(ethereum_g_train['Close'])
        plt.plot(ethereum_g_valid[['Close', 'predictions']])
        plt.legend(['History', 'Valid', 'Prediction'], loc='lower right')
        plt.show()

def graph_Stock_Graph(stock):

    if (stock == "binance"):
        plt.figure(figsize=(15, 5))
        plt.title("Binance Close History")
        plt.plot(binanceCoindf['Close'])
        plt.xlabel('Date', fontsize=18)
        plt.ylabel('Close Price')
        plt.show()

    elif (stock == "bitcoin"):
        plt.figure(figsize=(15, 5))
        plt.title("Bitcoin Close History")
        plt.plot(bitcoindf["Close"])
        plt.xlabel("Date", fontsize=10)
        plt.ylabel("Close Price", fontsize=10)
        plt.show()

    elif (stock == "cardano"):
        plt.figure(figsize=(15, 5))
        plt.title("Cardano Close History")
        plt.plot(cardanodf["Close"])
        plt.xlabel("Date", fontsize=10)
        plt.ylabel("Close Price", fontsize=10)
        plt.show()

    elif (stock == "dogecoin"):
        plt.figure(figsize=(15, 5))
        plt.title("Dogecoin Close History")
        plt.plot(dogecoindf["Close"])
        plt.xlabel("Date", fontsize=10)
        plt.ylabel("Close Price", fontsize=10)
        plt.show()

    elif (stock == "ethereum"):
        plt.figure(figsize=(15, 5))
        plt.title("Ethereum Close History")
        plt.plot(ethereumdf["Close"])
        plt.xlabel("Date", fontsize=10)
        plt.ylabel("Close Price", fontsize=10)
        plt.show()



"""
graph_Stock_Graph("binance")
graph_Stock_Predict("binance")

graph_Stock_Graph("bitcoin")
graph_Stock_Predict("bitcoin")

graph_Stock_Graph("cardano")
graph_Stock_Predict("cardano")

graph_Stock_Graph("dogecoin")
graph_Stock_Predict("dogecoin")

graph_Stock_Graph("ethereum")
graph_Stock_Predict("ethereum")
"""