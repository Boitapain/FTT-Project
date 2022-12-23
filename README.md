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
The API has 11 functions:
   1 -> register         #Register details of the user on the database
   2 -> login            #Login using the details that was registered
   3 -> price difference #Current price and price difference between stock and crypto
   4 -> stock_page       #View the stock page that was called 
   5 -> crypto_page      #View the crypto page that was called
   6 -> purchase         #Add purchase details to the database
   7 -> get_purchase     #Get purchase details from the database
   8 -> add_client       #Add client details to the database
   9 -> get_client       #Get client details from the database
  10 -> chatbot          #Interact with chatbot
  11 -> logout           #Logout of android app or website



The API allows the website to call a chatbox when it is needed.
