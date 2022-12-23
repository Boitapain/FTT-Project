# FinTech-Trader
FinTech-Trader (FTT) is a system allowing retail investors to invest in technology stocks and crypto assets without the support of stock brokers.
This system is divided into three distinctive applications :
- A mobile app that enables the retail investors to buy and sell their stocks.
- A website destined for brokers to advise their clients based on predictions of all the technology and crypto assets.
- An AI based on international Datasets, which will predict the prices of technology and crypto clients choose.

---
## FTT-Mobile
(TODO: add a screencast of the app and explain how it work)

---
## FTT-Web
(TODO: add screens of the front-end and explanations on how the website's work)

---
## FTT-AI
The API allows the FTT-Mobile App and the FTT-Website to send data through it and the API return data back to both when called.
The API revieves a json file with data for the databse i.e. register, login, purchase and client details. The file is trandfered
through the API to a python file which then transfers the data to a phpmyadmin database which was created for storing the data.
The details of the user is stored here with the password being stored using MD5 for confidentiality.

![image](https://user-images.githubusercontent.com/113469939/208953239-698af6af-79f0-465f-92f7-d1f30fa20248.png)

The API also allows the APP and the website to call the for the prices of the stock and crypto as well as the graphs with the predictions for
future investments.



The API allows the website to call a chatbox when it is needed.
