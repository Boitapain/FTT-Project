import pymysql
import sys
import json

from flask import jsonify

try:
    detailsdb = pymysql.connect(host='sql8.freesqldatabase.com',port=3306, user='sql8583755', passwd='AuCcUiq1hL', db="sql8583755")

except:
    sys.exit("Error connecting to the host")


db_cursor = detailsdb.cursor()

try:
    db_cursor.execute("CREATE DATABASE IF NOT EXISTS sql8583755;")
except pymysql.DatabaseError:
    sys.exit("Error creating the database")

db_cursor.execute('CREATE TABLE IF NOT EXISTS userdetails (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,'
                  ' first_name VARCHAR(255) NOT NULL,'
                  ' last_name VARCHAR(255) NOT NULL,'
                  ' email VARCHAR(255) NOT NULL UNIQUE,'
                  ' password VARCHAR(32) NOT NULL,'
                  ' financial_inst VARCHAR(225));')

db_cursor.execute('CREATE TABLE IF NOT EXISTS clients (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,'
                  ' first_name VARCHAR(255) NOT NULL,'
                  ' last_name VARCHAR(255) NOT NULL,'
                  ' email VARCHAR(255) NOT NULL,'
                  ' broker VARCHAR(225) NOT NULL);')

db_cursor.execute('CREATE TABLE IF NOT EXISTS purchasedetails (purchase_id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,'
                  ' email VARCHAR(255) NOT NULL,'
                  ' purchaseAmount VARCHAR(255) NOT NULL,'
                  ' asset VARCHAR(255) NOT NULL,'
                  ' date DATE NOT NULL);')


"""
db_cursor.execute("SHOW TABLES")
databaseList = db_cursor.fetchall()
for datatbase in databaseList:
    print(datatbase)
"""

def register(msg_received):
    db_cursor.execute('USE sql8583755')

    firstname = msg_received['firstname']
    lastname = msg_received['lastname']
    email = msg_received['email']
    password = msg_received['password']
    financial_inst = msg_received['financial_inst']

    select_query = "SELECT * FROM userdetails WHERE email = (%s)"
    db_cursor.execute(select_query, email)
    records = db_cursor.fetchall()
    if len(records) != 0:
        return "Another user used the email. Please chose another email."
    else:
        insert_query = "INSERT INTO userdetails (first_name, last_name, email, password, financial_inst) VALUES (%s, %s, %s, MD5(%s), %s)"
        insert_values = (firstname, lastname, email, password, financial_inst)
        try:
            db_cursor.execute(insert_query, insert_values)
            detailsdb.commit()
            return "successful"
        except Exception as e:
            print("Error while inserting the new record :", repr(e))
            return "failure"

def login(msg_received):
    db_cursor.execute('USE sql8583755;')

    email = msg_received['email']
    password = msg_received['password']

    select_query = "SELECT first_name, last_name FROM userdetails where email = (%s) and password = MD5(%s)"
    insert_values = (email, password)
    db_cursor.execute(select_query, insert_values)
    records = db_cursor.fetchall()

    if len(records) == 0:
        return "failure"
    else:
        return "successful"

def addclient(msg_received):
    db_cursor.execute('USE sql8583755')

    firstname = msg_received['firstname']
    lastname = msg_received['lastname']
    email = msg_received['email']
    broker = msg_received['broker']

    select_query = "SELECT * FROM clients WHERE email = (%s)"
    db_cursor.execute(select_query, email)
    records = db_cursor.fetchall()
    if len(records) != 0:
        return "Client already exists"
    else:
        insert_query = "INSERT INTO clients (first_name, last_name, email, broker) VALUES (%s, %s, %s, %s)"
        insert_values = (firstname, lastname, email, broker)
        try:
            db_cursor.execute(insert_query, insert_values)
            detailsdb.commit()
            return "successful"
        except Exception as e:
            print("Error while inserting the new record :", repr(e))
            return "failure"

def getClientsList(msg_received):
    db_cursor.execute("USE sql8583755")
    """
    first_name VARCHAR(255) NOT NULL,'
                      ' last_name VARCHAR(255) NOT NULL,'
                      ' email VARCHAR(255) NOT NULL UNIQUE,'
                      ' broker VARCHAR(225) NOT NULL);')
    """
    email = msg_received['email']

    client_details = {  "id":"",
                        "first_name": "",
                        "last_name": "",
                        "email": "",
                        "broker": ""}

    select_query = "SELECT * FROM clients where email = (%s)"
    db_cursor.execute(select_query, email)
    result = db_cursor.fetchone()
    if result:
        client_details["id"] = result[0]
        client_details["first_name"] = result[1]
        client_details["last_name"] = result[2]
        client_details["email"] = result[3]
        client_details["broker"] = result[4]

        return client_details
    else:
        return "No clients for this broker"

def add_purchase(msg_received):
    db_cursor.execute("USE sql8583755")

    email = msg_received['email']
    purchaseAmount = msg_received['purchaseAmount']
    asset = msg_received['asset']
    date = msg_received['date']

    insert_query = "INSERT INTO purchasedetails (email, purchaseAmount, asset, date) VALUES (%s, %s, %s, %s)"
    insert_values = (email, purchaseAmount, asset, date)

    try:
        db_cursor.execute(insert_query, insert_values)
        detailsdb.commit()
        return "successful"
    except Exception as e:
        print("Error while inserting the new record :", repr(e))
        return "failure"

def get_purchase(msg_received):
    db_cursor.execute("USE sql8583755")

    email = msg_received['email']

    purchase_details = {"purchase_id":"",
                        "email":"",
                        "purchaseAmount":"",
                        "asset":"",
                        "date":""}

    select_query = "SELECT * FROM purchasedetails where email = (%s)"
    db_cursor.execute(select_query, email)
    result = db_cursor.fetchone()
    if result:
        purchase_details["purchase_id"] = result[0]
        purchase_details["email"] = result[1]
        purchase_details["purchaseAmount"] = result[2]
        purchase_details["asset"] = result[3]
        purchase_details["date"] = result[4]

        return purchase_details
    else:
        return "No purchase details available"

try:
    detailsdb = pymysql.connect(host='sql8.freesqldatabase.com',port=3306, user='sql8583755', passwd='AuCcUiq1hL', db="sql8583755")
except:
    sys.exit("Error connecting to the host")

db_cursor = detailsdb.cursor()
