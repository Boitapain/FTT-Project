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