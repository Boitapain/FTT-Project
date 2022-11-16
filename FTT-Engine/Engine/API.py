import flask
import DetailsDB
import Crypto_Predict
import Stock_Predict

app = flask.Flask(__name__)

login = False

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

def price_diff():
    if login == True:
        return Crypto_Predict.crypto_Price_Diff()
        return Stock_Predict.stock_Price_Pred()
    else:
        return "Invalid request."

def stock_page():
    msg_received = flask.request.get_json()
    msg_subject = msg_received['subject']

    if msg_subject in ("amd", "apple", "gme", "tesla", "twitter"):
        return Stock_Predict.graph_Stock_Graph(msg_subject), Stock_Predict.graph_Stock_Predict(msg_subject)
    else:
        return "Invalid request."

def crypto_page():
    msg_received = flask.request.get_json()
    msg_subject = msg_received['subject']

    if msg_subject in ("binance", "bitcoin", "cardano", "dogecoin", "ethereum"):
        return Crypto_Predict.graph_Stock_Graph(msg_subject), Crypto_Predict.graph_Stock_Predict(msg_subject)
    else:
        return "Invalid request."

def purchase():
    msg_received = flask.request.get_json()
    msg_subject = msg_received['subject']

    if msg_subject == "purchase":
        return DetailsDB.purchase(msg_received)
    else:
        return "Invalid request."

app.run(host="127.0.0.1", port=5000, debug=True, threaded=True)

"""
 * Serving Flask app 'API' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 873-873-224
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
"""