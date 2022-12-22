import flask
from flask import jsonify, send_file
from flask_cors import CORS
import DetailsDB
import Crypto_Predict
import Stock_Predict
#import train_chatbox
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
    Sample Message:

    {"firstname": "Test",
    "lastname": "Lee",
    "email": "dl@mycit.ie",
    "password": 12345,
    "financial_inst": ""}
    """
    msg_received = flask.request.get_json(force=True)
    if msg_received != None:
        DetailsDB.register(msg_received)
        return "registered"
    else:
        return "Invalid request."

@app.route('/login', methods = ["GET", "POST"])
def login():
    """
    Sample Message:

    {"email": "dl@mycit.ie",
     "password": 12345}
    """
    msg_received = flask.request.get_json(force=True)
    global login
    if msg_received != None:
        return DetailsDB.login(msg_received)
        login = True
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
    Sample Message:

    {   "stock": ["amd", "tesla", "apple", "gme", "twitter"],
        "crypto": ["binance", "bitcoin", "cardano", "dogecoin", "ethereum"]}
    """
    msg_received = flask.request.get_json(force=True)
    global login
    if login == True:
        if "crypto" in msg_received:
            msg_subject = msg_received["crypto"]
            return jsonify(Crypto_Predict.crypto_Price_Diff(msg_subject))
        elif "stock" in msg_received:
            msg_subject = msg_received["stock"]
            return jsonify(Stock_Predict.stock_Price_Pred(msg_subject))
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
    Sample Message:

    {"stock": "tesla"}
    """
    msg_received = flask.request.get_json(force=True)
    if msg_received == "stock":
        diff = Stock_Predict.stock_Price_Pred(msg_received)
        graph_url = Stock_Predict.graph_Stock_Graph(msg_received)
        pred_graph_url = Stock_Predict.graph_Stock_Predict(msg_received)
        return jsonify(diff=diff, graph_url=graph_url, pred_graph_url=pred_graph_url)
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
    Sample Message:

    {"crypto": "bitcoin"}
    """
    msg_received = flask.request.get_json(force=True)
    if msg_received == "crypto":
        diff = Crypto_Predict.crypto_Price_Diff(msg_received)
        graph_url = Crypto_Predict.graph_crypto_Graph(msg_received)
        pred_graph_url = Crypto_Predict.graph_crypto_Predict(msg_received)
        return jsonify(diff=diff, graph_url=graph_url, pred_graph_url=pred_graph_url)
    else:
        return "Invalid request."

"""
If purchase is called, the app/website will send the message "purchase" with
the details of the purchase to the api and it will be stored in the database.
"""
@app.route('/purchase', methods = ["POST"])
def purchase():
    """
    Sample Message:

    {"email": "dl@mycit.ie",
     "purchaseAmount": "500.00",
     "asset": "amd",
     "date": "2022-12-12"}
    """
    msg_received = flask.request.get_json(force=True)
    if msg_received == "purchase":
        return DetailsDB.addclient(msg_received)
    else:
        return "Invalid request."

"""
If chatbot is called, the website will send the message "chatbot". The API will return
the chatbot to the website
"""
@app.route('/chatbot', methods = ["GET", "POST"])
def chatbot():
    """
        Sample Message:

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
    if (login == True):
        return DetailsDB.getClientsList(msg_received)
    else:
        return "not connected"

@app.route('/logout', methods=["GET"])
def logout():
    global login
    login = False
    if(login == False):
        return "succes"
    else:
        return "something went wrong"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5050, debug=True, threaded=True, use_reloader=False)

