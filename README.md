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
- > register         #Register details of the user on the database.
- > login            #Login using the details that was registered.
- > price difference #Current price and price difference between stock and crypto.
- > stock_page       #View the stock page that was called.
- > crypto_page      #View the crypto page that was called.
- > purchase         #Add purchase details to the database.
- > get_purchase     #Get purchase details from the database.
- > add_client       #Add client details to the database.
- > get_client       #Get client details from the database.
- > chatbot          #Interact with chatbot.
- > logout           #Logout of android app or website.

### > Register

The Register function allows the android app and website to register details of the user on the database.
The app or website sends a json file with the register details i.e., firstname, lastname, email, MD5 encrypted password and financial_inst.
An ID is created automatically when the details are passed through the API to the database. 

- Sample input from app or website
![image](https://user-images.githubusercontent.com/113469939/209335455-21ffc6bc-7bd5-4b40-b2a3-ae0e7ccc3f52.png)

The inputs are passed through the API into a function that passes the details to the database and returns successful if
complete. This then returns success in a json message to the app or website.

#### API function
![image](https://user-images.githubusercontent.com/113469939/209335775-e064442b-768b-4fe2-b788-cd375fe08154.png)

#### Database input
![image](https://user-images.githubusercontent.com/113469939/209335848-bdfa3e57-4c1d-4496-a6b9-5ee50b79f9bc.png)

#### Sample successful inputs to database
![image](https://user-images.githubusercontent.com/113469939/209335972-334b536e-66fb-47be-8438-ed43a567a767.png)
-----

### > Login

The login function takes a json message with the registered users email and password and sends it through the API to
the login function for the database. It is then checked if the login details matched an email and password stored in the
database. If it matches, it returns successful to the API which is then returned to the app or website. If it doesn't match,
it returns failure which is then sent to the app or website.

#### API Login Function
![image](https://user-images.githubusercontent.com/113469939/209336677-de32ad6d-1b67-49cd-8feb-3ee7e4daa973.png)

#### Login Function for Database
![image](https://user-images.githubusercontent.com/113469939/209336740-b0427ea5-5382-4f2f-85e4-6ccb3acb1fc5.png)
-----

### > Price Difference

The price difference function for the API allows the app and website to call for the current price and the price difference
of all the stock and crypto for the home page after the user logs into their account. The app and website send a json message with
the stock and crypto names to the API. The API uses these to call the crypto_Price_diff function for the crypto and the stock_Price_Pred
function for the stock. When these functions are called, the function runs through the subkeys of the stock and crypto key which then returns the
current and predicted prices of each in a dictionary. The API then returns the dictionary to the app and website in a json message.

#### API price_diff function
![image](https://user-images.githubusercontent.com/113469939/209338184-ddccb39b-efc1-4774-a5be-0ba6fd9a8889.png)

#### Crypto_Price_Diff function
![image](https://user-images.githubusercontent.com/113469939/209338350-347e1fe6-de61-4e2e-bc48-548a939ef628.png)
![image](https://user-images.githubusercontent.com/113469939/209338401-2b31ad74-c14d-4fac-bbe6-dca258790f89.png)

#### Stock_Price_Pred function
![image](https://user-images.githubusercontent.com/113469939/209338478-1769abe1-7b9a-4ddf-bc3b-155bf99bee55.png)
![image](https://user-images.githubusercontent.com/113469939/209338521-9a5a5ede-4fd8-46e5-a89a-88468e4cb0b8.png)

#### Sample json return message
![image](https://user-images.githubusercontent.com/113469939/209341006-f91e08ce-8eb8-4a3e-a1ef-8823f253796d.png)
![image](https://user-images.githubusercontent.com/113469939/209341039-93ca6584-76de-4cdb-8ca7-fdfbdde55ba0.png)
-----

### > Stock Page

The stock page function for the API allows the app and website to call a specific stock and see the current price and price 
difference, a graph showing the past prices and graph showing the predicted prices. The app and website sends a json message
with the stock called and will run through the functions stock_Price_Pred, graph_Stock_Graph and graph_Stock_Predict. When these functions
run, they return the prices, an image of the history graph and an image of the predicted graph. The graphs are encoded using base64 which then 
allows it to be sent over the API to the website and app in a json message. 

#### API stock_page function
![image](https://user-images.githubusercontent.com/113469939/209339842-14a8d47c-293e-4162-9ded-a803648f6974.png)

#### graph_Stock_Graph function
![image](https://user-images.githubusercontent.com/113469939/209340058-a1295079-208e-445b-811f-ecd2be195550.png)
![image](https://user-images.githubusercontent.com/113469939/209340109-a350b4b0-0c91-4d15-9a4f-bdf781162d60.png)

#### graph_Stock_Predict function
![image](https://user-images.githubusercontent.com/113469939/209339910-ed15bb8a-95d7-4613-a159-c2db1f76c277.png)
![image](https://user-images.githubusercontent.com/113469939/209339944-78591af5-74a7-4fc6-a5ab-b2b82886174d.png)
![image](https://user-images.githubusercontent.com/113469939/209339993-ad72744e-3ed2-49b1-af8b-73c64ce671fa.png)

#### Sample output of json response message
![image](https://user-images.githubusercontent.com/113469939/209341123-e48f4499-496a-4854-b415-9eb9e840cd2c.png)
-----

### > Crypto Page

The crypto page function for the API allows the app and website to call a specific crypto and see the current price and price 
difference, a graph showing the past prices and and graph showing the predicted prices. The app and website send a json message
with the crypto called and will run through the functions crypto_Price_Diff, graph_Crypto_Graph and graph_Crypto_Predict. When these functions
run, they return the prices, an image of the history graph and an image of the predicted graph. The graphs are encoded using base64 which then 
allows it to be sent over the API to the website and app in a json message. 

#### API crypto_page function
![image](https://user-images.githubusercontent.com/113469939/209340477-6fd26ad3-17bb-4b1a-a54f-d4d9b2450000.png)

#### graph_crypto_Graph function
![image](https://user-images.githubusercontent.com/113469939/209340726-152fd76a-102f-48fe-aec1-a1d663679bdd.png)
![image](https://user-images.githubusercontent.com/113469939/209340768-9f6b4498-9213-44f7-8318-7d4b467e61b0.png)

#### graph_crypto_Predict function
![image](https://user-images.githubusercontent.com/113469939/209340532-151b3335-fd2d-4134-9a30-31143679a585.png)
![image](https://user-images.githubusercontent.com/113469939/209340608-1db1046b-fccd-48b8-97f9-4f4b1a1b12af.png)
![image](https://user-images.githubusercontent.com/113469939/209340652-194e0a5c-f642-475f-9f6f-3fac440d82cd.png)

#### Sample output of json response message
![image](https://user-images.githubusercontent.com/113469939/209341197-0be4e705-78e5-4b81-a345-2a471cfd70f4.png)
-----

### > Purchase

The purchase function in the API receives the purchase details from the app or website and sends it to the add_purchase function 
for the database. It receives the email, purchaseAmount, asset and date. The purchasID is created automatically when inserted into 
the database. If successful, it return "successful in a json message back to the app or website.

#### API purchase function
![image](https://user-images.githubusercontent.com/113469939/209342810-d1e9a796-2ab6-4b1b-88c9-1d84bb6fd8ac.png)

#### add_purchase function
![image](https://user-images.githubusercontent.com/113469939/209342872-6a0477da-834c-45c5-a14d-c47524c0d941.png)

#### Sample successful inputs to database
![image](https://user-images.githubusercontent.com/113469939/209342987-f79052b3-1529-4185-a51b-7c5512784eed.png)
![image](https://user-images.githubusercontent.com/113469939/209342936-90ac9309-42bc-4c23-91c9-2dd371bf28b3.png)
-----

### > Get Purchase

The get purchase function in the API allows the website and app to request to see the purchases made by a specific email.
The app or website sends a json message with the users email to the API which is then forwarded onto the get_purchase function
for the database. If the email address matches purchases in the database, it returns all the purchases made by that user. The API 
then responds with the details in a json message.

#### API get_purchase function
![image](https://user-images.githubusercontent.com/113469939/209343753-c9780d6d-a537-440b-9360-e8950e66b5a4.png)

#### Get_purchase function for database
![image](https://user-images.githubusercontent.com/113469939/209343816-d0dc487c-a2aa-41c0-9a44-4a2ebd9ee99e.png)

#### Sample output of response from API
![image](https://user-images.githubusercontent.com/113469939/209344034-24010309-90bc-4173-97ec-02e8e882f3b6.png)
![image](https://user-images.githubusercontent.com/113469939/209344055-004e6dfc-0326-48d6-bc67-776ea15cc36e.png)
-----

### > Add Client

The add client function in the API allows the website to add a client to the database for the broker. It receives the 
clients firstname, lastname, email and broker in a json message and passes it to the function addclient for the database. 
The client gets added to the database and if successful it returns successful or returns failure if it doesn't get added.

#### API addclient function
![image](https://user-images.githubusercontent.com/113469939/209345506-99516583-b1a8-4892-b50f-abdddbd03966.png)

#### addclient function for database
![image](https://user-images.githubusercontent.com/113469939/209345551-d971b6d8-4c7b-40ee-ac9e-79eeb690b59c.png)

#### Sample output response from API
![image](https://user-images.githubusercontent.com/113469939/209345580-d9a0aa91-5451-47a3-9b5e-2ca48ac3cb56.png)
![image](https://user-images.githubusercontent.com/113469939/209345659-7b1d2785-c235-491c-b1b8-382c23e07d0d.png)
-----

### > Get Client

The get client function on the API allows the website to access and view the clients when needed. It returns a json message
with the details of the client, it is looking for.

#### API getClientList function
![image](https://user-images.githubusercontent.com/113469939/209345900-7aad2348-08c2-40a6-b0fa-316b92e8e8f5.png)

#### getClientList function from the database
![image](https://user-images.githubusercontent.com/113469939/209346007-b4287e04-e520-4d2f-9332-e24e40f75a77.png)

#### Sample output response from API
![image](https://user-images.githubusercontent.com/113469939/209346092-563664c0-2a69-44b3-8c9a-104246bf2da1.png)
![image](https://user-images.githubusercontent.com/113469939/209346130-f9037acd-8f80-40dc-9deb-248c304b25ee.png)
-----

### > Chatbot

The chatbot allows the website to send messages from the user to the API and receive a response. It is able to understand 
misspellings of the message sent. It returns the response in a json message back to the website.

#### API chatbot function
![image](https://user-images.githubusercontent.com/113469939/209346422-16dee8b4-6ca8-4bad-bafb-fe3822ffe5c3.png)

#### Sample chatbot response
![image](https://user-images.githubusercontent.com/113469939/209346513-8730d32f-fd9f-4b12-86e5-4b5ca8cefd00.png)
![image](https://user-images.githubusercontent.com/113469939/209346570-0cbc8ebc-4759-460f-b1ac-663375d7fb96.png)
-----

### > Logout

The logout function changes the login variable from True to False when called. It returns a response saying "success" when 
it is run. 

#### API logout function
![image](https://user-images.githubusercontent.com/113469939/209346793-68021901-a8af-4910-8f8b-f44fd1728719.png)

#### Sample logout response
![image](https://user-images.githubusercontent.com/113469939/209346870-ceb62261-b377-4261-a3fd-56f1ee2d351d.png)
![image](https://user-images.githubusercontent.com/113469939/209346899-3880a1c9-fd94-4ccf-8ec6-258a4307e241.png)

---
