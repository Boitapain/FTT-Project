from unittest import TestCase
import json
import requests


class Test(TestCase):
    global API_URL, REGISTER_SAMPLE, STOCK_CRYPTO_SAMPLE
    API_URL = "http://127.0.0.1:5050"
    REGISTER_SAMPLE = {"firstname": "David",
                       "lastname": "Lee",
                       "email": "dl@mycit.ie",
                       "password": 12345,
                       "financial_inst": ""}
    STOCK_CRYPTO_SAMPLE = {"stock": "Tesla",
                           "crypto": "Bitcoin"}

    def test_register(self):
        response = requests.post(f"{API_URL}/register", json=REGISTER_SAMPLE)
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        login = {"email": "dl@mycit.ie",
                 "password": 12345}
        response = requests.get(f"{API_URL}/login", json=login)
        self.assertEqual(response.status_code, 200)

        login = {"email": "dllll@mycit.ie",
                 "password": 12345}
        response = requests.get(f"{API_URL}/login", json=login)
        self.assertEqual(response.status_code, 200)

