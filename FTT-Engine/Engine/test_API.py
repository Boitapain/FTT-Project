import subprocess
from unittest import TestCase
import json
import requests
import datetime
import base64


class Test_API(TestCase):
    global API_URL, LOGIN, REGISTER_SAMPLE_1, REGISTER_SAMPLE_2, STOCK_CRYPTO_SAMPLE, CRYPTO_TEST, STOCK_TEST, PURCHASE_SAMPLE, GET_PURCHASE_SAMPLE, ADD_CLIENT_SAMPLE, TEST_GET_CLIENT, CHATBOX_TEST_1, CHATBOX_TEST_2, CHATBOX_TEST_3, HEADERS
    API_URL = "http://127.0.0.1:5050"
    HEADERS = {"Content-Type": "application/json"}

    REGISTER_SAMPLE_1 = {"firstname": "David",
                       "lastname": "Lee",
                       "email": "dl@mycit.ie",
                       "password": 12345,
                       "financial_inst": ""}
    REGISTER_SAMPLE_2 = {"firstname": "Vincent",
                         "lastname": "Bullion",
                         "email": "vb@mycit.ie",
                         "password": 23456,
                         "financial_inst": "FTT"}

    LOGIN = {"email": "dl@mycit.ie",
             "password": 12345}

    STOCK_CRYPTO_SAMPLE = {
        "stock": ["amd", "tesla", "apple", "gme", "twitter"],
        "crypto": ["binance", "bitcoin", "cardano", "dogecoin", "ethereum"]}

    CRYPTO_TEST = {"crypto": "bitcoin"}

    STOCK_TEST = {"stock": "tesla"}

    PURCHASE_SAMPLE_1 = {"email": "dl@mycit.ie",
                       "purchaseAmount": "500.00",
                       "asset": "amd",
                       "date": "2022-12-12"
                       }
    PURCHASE_SAMPLE_1 = {"email": "vb@mycit.ie",
                         "purchaseAmount": "2000.00",
                         "asset": "bitcoin",
                         "date": "2022-12-12"
                         }

    GET_PURCHASE_SAMPLE = {"email": "dl@mycit.ie"}

    ADD_CLIENT_SAMPLE = {"firstname": "Alan",
                         "lastname": "Healy",
                         "email": "ah@mycit.ie",
                         "broker": "David"}

    TEST_GET_CLIENT = {"email": "ah@mycit.ie"}

    CHATBOX_TEST_1 = {"message": "Hello"}
    CHATBOX_TEST_2 = {"message": "crypto"}
    CHATBOX_TEST_3 = {"message": "deposit"}

    def test_register(self):
        response = requests.post(f"{API_URL}/register", json=REGISTER_SAMPLE_1)
        self.assertEqual(response.status_code, 200)
        print(response.text)
        response = requests.post(f"{API_URL}/register", json=REGISTER_SAMPLE_2)
        self.assertEqual(response.status_code, 200)
        print(response.text)
        response = requests.post(f"{API_URL}/register", json=REGISTER_SAMPLE_1)
        self.assertEqual(response.status_code, 200)
        print(response.text)

    def test_login(self):
        response = requests.get(f"{API_URL}/login", json=LOGIN)
        self.assertEqual(response.status_code, 200)
        print(response.text)

        login = {"email": "dllll@mycit.ie",
                 "password": 12345}
        response = requests.get(f"{API_URL}/login", json=login)
        self.assertEqual(response.status_code, 200)
        print(response.text)

        response = requests.get(f"{API_URL}/login", json=LOGIN)
        self.assertEqual(response.status_code, 200)
        print(response.text)

    def test_price_diff(self):
        response = requests.get(f"{API_URL}/pricediff", json=STOCK_CRYPTO_SAMPLE, headers=HEADERS)
        self.assertEqual(response.status_code, 200)
        print(response.text)

    def test_stock_page(self):
        response = requests.get(f"{API_URL}/stockpage", json=STOCK_TEST)
        self.assertEqual(response.status_code, 200)
        response_json = response.json()
        for key, file in (("graph_url", "stock1.png"), ("pred_graph_url", "stock2.png")):
            image_data_b64 = response_json[key]
            image_data = base64.b64decode(image_data_b64)
            with open(f"Test_image/{file}", "wb") as f:
                f.write(image_data)
        print(response.text)

    def test_crypto_page(self):
        response = requests.get(f"{API_URL}/cryptopage", json=CRYPTO_TEST)
        self.assertEqual(response.status_code, 200)
        response_json = response.json()
        for key, file in (("graph_url", "crypto1.png"), ("pred_graph_url", "crypto2.png")):
            image_data_b64 = response_json[key]
            image_data = base64.b64decode(image_data_b64)
            with open(f"Test_image/{file}", "wb") as f:
                f.write(image_data)
        print(response.text)

    def test_purchase(self):
        response = requests.post(f"{API_URL}/purchase", json=PURCHASE_SAMPLE, headers=HEADERS)
        self.assertEqual(response.status_code, 200)
        print(response.text)

    def test_addclient(self):
        response = requests.post(f"{API_URL}/addclient", json=ADD_CLIENT_SAMPLE)
        self.assertEqual(response.status_code, 200)
        print(response.text)

    def test_get_client_list(self):
        response = requests.post(f"{API_URL}/getclients", json=TEST_GET_CLIENT)
        self.assertEqual(response.status_code, 200)
        print(response.text)

    def test_chatbot(self):
        response = requests.post(f"{API_URL}/chatbot", json=CHATBOX_TEST_1)
        self.assertEqual(response.status_code, 200)
        print(response.text)
        response = requests.post(f"{API_URL}/chatbot", json=CHATBOX_TEST_2)
        self.assertEqual(response.status_code, 200)
        print(response.text)
        response = requests.post(f"{API_URL}/chatbot", json=CHATBOX_TEST_3)
        self.assertEqual(response.status_code, 200)
        print(response.text)

    def test_get_purchase(self):
        response = requests.post(f"{API_URL}/getpurchase", json=GET_PURCHASE_SAMPLE)
        self.assertEqual(response.status_code, 200)
        print(response.text)


    def test_logout(self):
        response = requests.get(f"{API_URL}/logout")
        self.assertEqual(response.status_code, 200)
        print(response.text)
