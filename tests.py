import unittest
import os
import json
from api import create_app
import base64

class EncrytDecryptTest(unittest.TestCase):
    """
    Encrypt Decrypt Test Cases
    """
    def setUp(self):
        """
        Test Setup
        """
        self.app = create_app()
        self.client = self.app.test_client

    def test_health_check(self):
        result = self.client().get('/api/health')
        self.assertEqual(result.status_code,200)
        self.assertEqual(result.get_json()['Output'],"OK")

    def test_encrypt_without_data(self):
        api_response = self.client().post('/api/encrypt')
        result = api_response.get_json()
        self.assertEqual(api_response.status_code,400)
        self.assertEqual(result['Status'],'error')
        self.assertEqual(result['Message'],'Request Body Empty')

    def test_encrypt_with_data_blank(self):
        api_response = self.client().post('/api/encrypt' , json=dict())
        result = api_response.get_json()
        self.assertEqual(api_response.status_code,400)
        self.assertEqual(result['Status'],'error')
        self.assertEqual(result['Message'],'Request Body Empty')

    def test_encrypt_with_empty_input(self):
        api_response = self.client().post('/api/encrypt' , json=dict(input=''))
        result = api_response.get_json()
        self.assertEqual(api_response.status_code,400)
        self.assertEqual(result['Status'],'error')
        self.assertEqual(result['Message'],'Input String Empty')

    def test_encrypt_with_data(self):
        api_response = self.client().post('/api/encrypt', json=dict(input='My String to encrypt'))
        result = api_response.get_json()
        self.assertEqual(api_response.status_code,200)
        self.assertEqual(result['Status'],'success')
        self.assertEqual(result['Output'], 'TXkgU3RyaW5nIHRvIGVuY3J5cHQ=')

    def test_decrypt_without_data(self):
        api_response = self.client().post('/api/decrypt')
        result = api_response.get_json()
        self.assertEqual(api_response.status_code,400)
        self.assertEqual(result['Status'],'error')
        self.assertEqual(result['Message'],'Request Body Empty')

    def test_decrypt_with_data_blank(self):
        api_response = self.client().post('/api/decrypt' , json=dict())
        result = api_response.get_json()
        self.assertEqual(api_response.status_code,400)
        self.assertEqual(result['Status'],'error')
        self.assertEqual(result['Message'],'Request Body Empty')

    def test_decrypt_with_empty_input(self):
        api_response = self.client().post('/api/decrypt' , json=dict(input=''))
        result = api_response.get_json()
        self.assertEqual(api_response.status_code,400)
        self.assertEqual(result['Status'],'error')
        self.assertEqual(result['Message'],'Input String Empty')

    def test_decrypt_with_data(self):
        api_response = self.client().post('/api/decrypt', json=dict(input='TXkgU3RyaW5nIHRvIGVuY3J5cHQ='))
        result = api_response.get_json()
        self.assertEqual(api_response.status_code,200)
        self.assertEqual(result['Status'],'success')
        self.assertEqual(result['Output'],'My String to encrypt')

    def test_decrypt_error(self):
        api_response = self.client().post('/api/decrypt', json=dict(input='My String to encrypt'))
        result = api_response.get_json()
        self.assertEqual(api_response.status_code,500)
        self.assertEqual(result['Status'],'error')
        self.assertEqual(result['Message'],'Something Went Wrong.')

if __name__ == "__main__":
  unittest.main()
