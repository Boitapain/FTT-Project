import flask
from flask_cors import CORS
import DetailsDB
import Crypto_Predict
import Stock_Predict


app = flask.Flask(__name__)
CORS(app)

login = False

"""
Chat between app/website with login/register.
App/Website needs to send key word "login" or "register" with details
to save to database.
"""
@app.route('/', methods = ["GET", "POST"])
def chat():
    msg_received = flask.request.get_json()
    msg_subject = msg_received['subject']

    if msg_subject == "register":
        return DetailsDB.register(msg_received)
    elif msg_subject == "login":
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
    if login == True:
        return Crypto_Predict.crypto_Price_Diff()
        return Stock_Predict.stock_Price_Pred()
    else:
        return "Invalid request."

"""
If stock page is called, app/website will send name of stock
-> "amd", "apple", "gme", "tesla", "twitter" to api and api will
return the graphs (current and prediciton)
"""
@app.route('/stockpage', methods = ["GET", "POST"])
def stock_page():
    msg_received = flask.request.get_json()
    msg_subject = msg_received['subject']

    if msg_subject in ("amd", "apple", "gme", "tesla", "twitter"):
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
    msg_received = flask.request.get_json()
    msg_subject = msg_received['subject']

    if msg_subject in ("binance", "bitcoin", "cardano", "dogecoin", "ethereum"):
        return Crypto_Predict.crypto_Price_Diff(msg_subject), Crypto_Predict.graph_Stock_Graph(msg_subject), Crypto_Predict.graph_Stock_Predict(msg_subject)
    else:
        return "Invalid request."

"""
If purchase is called, the app/website will send the message "purchase" with
the details of the purchase to the api and it will be stored in the database.
"""
@app.route('/purchase', methods = ["GET", "POST"])
def purchase():
    msg_received = flask.request.get_json()
    msg_subject = msg_received['subject']

    if msg_subject == "purchase":
        return DetailsDB.purchase(msg_received)
    else:
        return "Invalid request."

app.run(host="127.0.0.1", port=5000, debug=True, threaded=True)

