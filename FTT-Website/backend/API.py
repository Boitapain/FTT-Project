import flask
from flask_cors import CORS
import DetailsDB
# import Crypto_Predict
# import Stock_Predict

app = flask.Flask(__name__)
CORS(app)

login = False


@app.route('/logout', methods = ["GET", "POST"])
def logout():
    global login
    login = False
    if(login == False):
        return "succes"
    else:
        return "something went wrong"

@app.route('/islogin', methods = ["GET", "POST"])
def islogin():
    global login
    if(login):
        return "true"
    else:
        return "false"


@app.route('/getclients', methods = ["GET", "POST"])
def getClientList():
    global login
    msg_received = flask.request.get_json()
    
    if(login == True):
        return DetailsDB.getClientsList(msg_received)
    else:
        return "not connected"


@app.route('/', methods = ["GET", "POST"])
def chat():
    global login
    
    msg_received = flask.request.get_json()
    msg_subject = msg_received['subject']
    
    if msg_subject == "register":
        return DetailsDB.register(msg_received)
    elif msg_subject == "login":
        result = DetailsDB.login(msg_received)
        if (result == "successful"):
            login = True
        return result
        
    else:
        return "Invalid request."
    
"""
If login is true, the app/website sends the stock/crypto names
to the api and the api returns current price &
price difference for each crypto/stock.
"""

@app.route('/pricediff', methods = ["GET", "POST"])
def price_diff():
    global login
    if login == True:
        return Crypto_Predict.crypto_Price_Diff()
        return Stock_Predict.stock_Price_Pred()

"""
If stock page is called, app/website will send name of stock
-> "amd", "apple", "gme", "tesla", "twitter" to api and api will
return the graphs (current and prediciton)
"""
@app.route('/stockpage', methods = ["GET", "POST"])
def stock_page():
    msg_received = flask.request.get_json(force=True)
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
    msg_received = flask.request.get_json(force=True)
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
    msg_received = flask.request.get_json(force=True)
    msg_subject = msg_received['subject']

    if msg_subject == "purchase":
        return DetailsDB.purchase(msg_received)
    else:
        return "Invalid request."

if __name__ == "__main__":
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

 Run: python -m flask --app .\API.py run
"""