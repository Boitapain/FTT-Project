import base64

import flask
from flask import jsonify, send_file
from flask_cors import CORS
import DetailsDB
import Crypto_Predict
import Stock_Predict
import train_chatbox
import chatapp

app = flask.Flask(__name__)
CORS(app)
login = False

"""
Open Page with group names
"""
@app.route('/')
def startup():
    return "Group17 Project\n\nDavid Lee\nEthan Ponce\nVincent Bullion\nJérémie Blanc"

"""
If register a, the app/website sends the stock/crypto names
to the api and the api returns current price &
price difference for each crypto/stock.
"""

@app.route('/register', methods = ["GET", "POST"])
def register():
    """
    Sample Input Message:

    {"firstname": "Test",
    "lastname": "Lee",
    "email": "dl@mycit.ie",
    "password": 12345,
    "financial_inst": ""}
    """
    msg_received = flask.request.get_json(force=True)
    if msg_received != None:
        result = DetailsDB.register(msg_received)
        return "registered"
    else:
        return "Invalid request."

@app.route('/login', methods = ["GET", "POST"])
def login():
    """
    Sample Input Message:

    {"email": "dl@mycit.ie",
     "password": 12345}
    """
    msg_received = flask.request.get_json(force=True)
    global login
    if msg_received != None:
        login_pass_fail = DetailsDB.login(msg_received)
        if login_pass_fail == "successful":
            login = True
            return "success"
        else:
            return "failure"
    else:
        return "Invalid request."

"""
If login is true, the app/website sends the stock/crypto names
to the api and the api returns current price &
price difference for each crypto/stock.
"""
@app.route('/pricediff', methods = ["GET", "POST"])
def price_diff():
    """
    Sample Input Message:

    {   "stock": ["amd", "tesla", "apple", "gme", "twitter"],
        "crypto": ["binance", "bitcoin", "cardano", "dogecoin", "ethereum"]}
    """
    msg_received = flask.request.get_json(force=True)
    global login
    if login == True:
        if "crypto" in msg_received or "stock" in msg_received:
            crypto =  Crypto_Predict.crypto_Price_Diff(msg_received)
            stock =  Stock_Predict.stock_Price_Pred(msg_received)
            return jsonify(crypto=crypto, stock=stock)
        else:
            return "Invalid request."

"""
If stock page is called, app/website will send name of stock
-> "amd", "apple", "gme", "tesla", "twitter" to api and api will
return the graphs (current and prediciton)
"""
@app.route('/stockpage', methods = ["GET", "POST"])
def stock_page():
    """
    Sample Input Message:

    {"stock": "tesla"}
    """
    msg_received = flask.request.get_json(force=True)
    if "stock" in msg_received:
        diff = Stock_Predict.stock_Price_Pred(msg_received)
        graph_url = Stock_Predict.graph_Stock_Graph(msg_received)
        pred_graph_url = Stock_Predict.graph_Stock_Predict(msg_received)

        with open(graph_url, "rb") as f:
            graph_data = f.read()
        with open(pred_graph_url, "rb") as f:
            pred_graph_data = f.read()

        graph_data_b64 = base64.b64encode(graph_data).decode("utf-8")
        pred_graph_data_b64 = base64.b64encode(pred_graph_data).decode("utf-8")

        return jsonify(diff=diff, graph_url=graph_data_b64, pred_graph_url=pred_graph_data_b64)
    else:
        return "Invalid request."

"""
If crypto page is called, app/website will send name of crypto
-> "binance", "bitcoin", "cardano", "dogecoin", "ethereum" to api and api will
return the graphs (current and prediciton)
"""
@app.route('/cryptopage', methods = ["GET", "POST"])
def crypto_page():
    """
    Sample Input Message:

    {"crypto": "bitcoin"}
    """
    msg_received = flask.request.get_json(force=True)
    if "crypto" in msg_received:
        diff = Crypto_Predict.crypto_Price_Diff(msg_received)
        graph_url = Crypto_Predict.graph_crypto_Graph(msg_received)
        pred_graph_url = Crypto_Predict.graph_crypto_Predict(msg_received)

        with open(graph_url, "rb") as f:
            graph_data = f.read()
        with open(pred_graph_url, "rb") as f:
            pred_graph_data = f.read()

        graph_data_b64 = base64.b64encode(graph_data).decode("utf-8")
        pred_graph_data_b64 = base64.b64encode(pred_graph_data).decode("utf-8")

        return jsonify(diff=diff, graph_url=graph_data_b64, pred_graph_url=pred_graph_data_b64)
    else:
        return "Invalid request."

"""
If purchase is called, the app/website will send the message "purchase" with
the details of the purchase to the api and it will be stored in the database.
"""
@app.route('/purchase', methods = ["GET", "POST"])
def purchase():
    """
    Sample Input Message:

    {"email": "dl@mycit.ie",
     "purchaseAmount": "500.00",
     "asset": "amd",
     "date": "2022-12-12"}
    """
    msg_received = flask.request.get_json(force=True)
    if msg_received != None:
        result =  DetailsDB.add_purchase(msg_received)
        if result == "successful":
            return result
        else:
            return result
    else:
        return "Invalid request"

@app.route('/getpurchase', methods = ["GET", "POST"])
def get_purchase():
    global login
    msg_received = flask.request.get_json(force=True)
    if msg_received != None:
        results = DetailsDB.get_purchase(msg_received)
        return jsonify(results)
    else:
        return "Invalid request"

"""
If chatbot is called, the website will send the message "chatbot". The API will return
the chatbot to the website
"""
@app.route('/chatbot', methods = ["GET", "POST"])
def chatbot():
    """
        Sample Input Message:

        {"message": "Hello"}
    """
    msg_received = flask.request.get_json(force=True)["message"]

    if msg_received != None:
        response = chatapp.chatbot_response(msg_received)
        return jsonify({'response': response})
    else:
        return "Invalid request"

@app.route('/addclient', methods = ["POST"])
def addclient():
    """
    Sample Message:

    {"firstname": "Alan",
     "lastname": "Healy",
     "email": "ah@mycit.ie",
     "broker": "Steven"}
    """
    msg_received = flask.request.get_json(force=True)

    if msg_received != None:
        return DetailsDB.addclient(msg_received)
    else:
        return "Invalid request."

@app.route('/getclients', methods=["GET", "POST"])
def getClientList():
    """
        Sample Message:

        {"email": "ah@mycit.ie"}
        """
    global login
    msg_received = flask.request.get_json(force=True)
    if msg_received != None:
        result = DetailsDB.getClientsList(msg_received)
        return jsonify(result)
    else:
        return "Invalid request"

@app.route('/logout', methods=["GET"])
def logout():
    global login
    login = False
    if(login == False):
        return "success"
    else:
        return "failure"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5050, debug=True, threaded=True, use_reloader=False)

