import pymysql
import sys
import flask
import json

app = flask.Flask(__name__)

try:
    detailsdb = pymysql.connect(host='127.0.0.1',port=3306, user='group17', passwd='group17', db="details_db")
except:
    sys.exit("Error connecting to the host. Please check your inputs.")


db_cursor = detailsdb.cursor()

try:
    db_cursor.execute("CREATE DATABASE IF NOT EXISTS details_db")
except pymysql.DatabaseError:
    sys.exit("Error creating the database. Check if database already exists!")

db_cursor.execute('CREATE TABLE IF NOT EXISTS userdetails (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,'
                  ' first_name VARCHAR(255) NOT NULL,'
                  ' last_name VARCHAR(255) NOT NULL,'
                  ' email VARCHAR(255) NOT NULL UNIQUE,'
                  ' password VARCHAR(32) NOT NULL,'
                  ' financial_inst VARCHAR(225))')

@app.route('/register', methods = ["GET", "POST"])
def chat():
    msg_received = flask.request.get_json()
    msg_subject = msg_received["subject"]

    if msg_subject == "register":
        return register(msg_received)
    elif msg_subject == "login":
        return login(msg_received)
    else:
        return "Invalid request."

def register(msg_received):
    firstname = msg_received["firstname"]
    lastname = msg_received["lastname"]
    email = msg_received["email"]
    password = msg_received["password"]
    financial_inst = msg_received["financial_inst"]

    select_query = "SELECT * FROM users where email = " + "'" + email + "'"
    db_cursor.execute(select_query)
    records = db_cursor.fetchall()
    if len(records) != 0:
        return "Another user used the email. Please chose another email."

    insert_query = "INSERT INTO userdetails (first_name, last_name, email, password, financial_inst) VALUES (%s, %s, %s, MD5(%s), %s)"
    insert_values = (firstname, lastname, email, password, financial_inst)
    try:
        db_cursor.execute(insert_query, insert_values)
        detailsdb.commit()
        return "success"
    except Exception as e:
        print("Error while inserting the new record :", repr(e))
        return "failure"

def login(msg_received):
    email = msg_received["email"]
    password = msg_received["password"]

    select_query = "SELECT first_name, last_name FROM users where email = " + "'" + email + "' and password = " + "MD5('" + password + "')"
    db_cursor.execute(select_query)
    records = db_cursor.fetchall()

    if len(records) == 0:
        return "failure"
    else:
        return "success"
    try:
        detailsdb = pymysql.connect(host='127.0.0.1', port=3306, user='group17', passwd='group17')
    except:
        sys.exit("Error connecting to the host. Please check your inputs.")

db_cursor = detailsdb.cursor()
app.run(host="0.0.0.0", port=5000, debug=True, threaded=True)

"""
 * Serving Flask app 'DetailsDB' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 124-208-133
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://192.168.0.156:5000/ (Press CTRL+C to quit)
 """