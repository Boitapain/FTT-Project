from unittest import TestCase
import json
import requests
import datetime


class Test(TestCase):
    global API_URL, LOGIN, REGISTER_SAMPLE, STOCK_CRYPTO_SAMPLE, CRYPTO_TEST, STOCK_TEST, PURCHASE_SAMPLE ,ADD_CLIENT_SAMPLE, TEST_GET_CLIENT, CHATBOX_TEST
    API_URL = "http://127.0.0.1:5050"


    REGISTER_SAMPLE = {"firstname": "David",
                       "lastname": "Lee",
                       "email": "dl@mycit.ie",
                       "password": 12345,
                       "financial_inst": ""}

    LOGIN = {"email": "dl@mycit.ie",
             "password": 12345}

    STOCK_CRYPTO_SAMPLE = {
        "stock": ["amd", "tesla", "apple", "gme", "twitter"],
        "crypto": ["binance", "bitcoin", "cardano", "dogecoin", "ethereum"]}

    CRYPTO_TEST = {"crypto": "amd"}

    STOCK_TEST = {"stock": "tesla"}

    PURCHASE_SAMPLE = {"email": "dl@mycit.ie",
                       "purchaseAmount": 500,
                       "asset": "amd",
                       "date": datetime.datetime.now().isoformat()
                       }

    ADD_CLIENT_SAMPLE = {"firstname": "Alan",
                         "lastname": "Healy",
                         "email": "ah@mycit.ie",
                         "broker": "Steven"}

    TEST_GET_CLIENT = {"email": "ah@mycit.ie"}

    CHATBOX_TEST = {"chatbot":""}

    def test_register(self):
        response = requests.post(f"{API_URL}/register", json=REGISTER_SAMPLE)
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = requests.get(f"{API_URL}/login", json=LOGIN)
        self.assertEqual(response.status_code, 200)
        """
        login = {"email": "dllll@mycit.ie",
                 "password": 12345}
        response = requests.get(f"{API_URL}/login", json=LOGIN)
        self.assertEqual(response.status_code, 200)
        """

    def test_price_diff(self):
        response = requests.get(f"{API_URL}/pricediff", json=STOCK_CRYPTO_SAMPLE)
        self.assertEqual(response.status_code, 200)

    def test_stock_page(self):
        response = requests.get(f"{API_URL}/stockpage", json=STOCK_TEST)
        self.assertEqual(response.status_code, 200)

    def test_crypto_page(self):
        response = requests.get(f"{API_URL}/cryptopage", json=CRYPTO_TEST)
        self.assertEqual(response.status_code, 200)

    def test_purchase(self):
        response = requests.get(f"{API_URL}/purchase", json=PURCHASE_SAMPLE)
        self.assertEqual(response.status_code, 200)

    def test_addclient(self):
        response = requests.get(f"{API_URL}/addclient", json=ADD_CLIENT_SAMPLE)
        self.assertEqual(response.status_code, 200)

    def test_get_client_list(self):
        response = requests.get(f"{API_URL}/getclients", json=TEST_GET_CLIENT)
        self.assertEqual(response.status_code, 200)

    def test_chatbot(self):
        response = requests.get(f"{API_URL}/chatbot", json=CHATBOX_TEST)
        self.assertEqual(response.status_code, 200)


