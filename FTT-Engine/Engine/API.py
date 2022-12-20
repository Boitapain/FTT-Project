import flask
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
    msg_received = flask.request.get_json(force=True)
    if msg_received != None:
        DetailsDB.register(msg_received)
        return "registered"
    else:
        return "Invalid request."

@app.route('/login', methods = ["GET", "POST"])
def login():
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
    msg_received = flask.request.get_json(force=True)
    global login
    if login == True:
        if "crypto" in msg_received:
            msg_subject = msg_received["crypto"]
            return Crypto_Predict.crypto_Price_Diff(msg_subject)
        elif "stock" in msg_received:
            msg_subject = msg_received["stock"]
            return Stock_Predict.stock_Price_Pred(msg_subject)
    else:
        return "Invalid request."

"""
If stock page is called, app/website will send name of stock
-> "amd", "apple", "gme", "tesla", "twitter" to api and api will
return the graphs (current and prediciton)
"""
@app.route('/stockpage', methods = ["GET", "POST"])
def stock_page():
    msg_received = flask.request.get_json(force=True)

    if msg_received in ("amd", "apple", "gme", "tesla", "twitter"):
        msg_subject = msg_received
        return Stock_Predict.graph_Stock_Predict(msg_subject), Stock_Predict.graph_Stock_Graph(msg_subject), Stock_Predict.graph_Stock_Predict(msg_subject)
    else:
        return "Invalid request."

"""
If crypto page is called, app/website will send name of crypto
-> "binance", "bitcoin", "cardano", "dogecoin", "ethereum" to api and api will
return the graphs (current and prediciton)
"""
@app.route('/cryptopage', methods = ["GET", "POST"])
def crypto_page():
    msg_received = flask.request.get_json(force=True)
    if msg_received in ("binance", "bitcoin", "cardano", "dogecoin", "ethereum"):
        msg_subject = msg_received[""]
        return Crypto_Predict.crypto_Price_Diff(msg_subject), Crypto_Predict.graph_Stock_Graph(msg_subject), Crypto_Predict.graph_Stock_Predict(msg_subject)
    else:
        return "Invalid request."

"""
If purchase is called, the app/website will send the message "purchase" with
the details of the purchase to the api and it will be stored in the database.
"""
@app.route('/purchase', methods = ["GET", "POST"])
def purchase():
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
    msg_received = flask.request.get_json(force=True)

    if msg_received == "chatbot":
        return chatapp.return_chatbot()
    else:
        return "Invalid request"

@app.route('/addclient', methods = ["GET", "POST"])
def addclient():
    msg_received = flask.request.get_json(force=True)

    if msg_received != None:
        return DetailsDB.addclient(msg_received)
    else:
        return "Invalid request."

@app.route('/getclients', methods=["GET", "POST"])
def getClientList():
    global login
    msg_received = flask.request.get_json(force=True)
    if (login == True):
        return DetailsDB.getClientsList(msg_received)
    else:
        return "not connected"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5050, debug=True, threaded=True, use_reloader=False)

