import unittest
from app import app
from flask import json

class FlaskBookshelfTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_home_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_home_data(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/')

        # assert the response data
        self.assertEqual(result.data, b'Hello, World!')


    def test_create_code_status(self):
        # sends HTTP GET request to the application
        # on the specified path

        data_j = json.dumps({"phone": "2014563334"})
        result = self.app.post('/createCode', data=data_j, content_type='application/json')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_check_sms_status(self):
        # sends HTTP GET request to the application
        # on the specified path

        data_j = json.dumps({"code": "1234","phone": "9999999999"})
        result = self.app.post('/checkCode', data=data_j, content_type='application/json')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_check_sms_data(self):
        # sends HTTP GET request to the application
        # on the specified path

        data_j = json.dumps({"code": "1234","phone": "9999999999"})
        result = self.app.post('/checkCode', data=data_j, content_type='application/json')

        # assert the status code of the response
        self.assertEqual(result.data, b'"User and SMS code don\'t exist"')

    def test_check_user_verified_status(self):
        # sends HTTP GET request to the application
        # on the specified path

        data_j = json.dumps({"code": "1234","phone": "9999999999"})
        result = self.app.post('/isVerified', data=data_j, content_type='application/json')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)


    def test_check_user_verified_data(self):
        # sends HTTP GET request to the application
        # on the specified path

        data_j = json.dumps({"code": "1234","phone": "9999999999"})
        result = self.app.post('/isVerified', data=data_j, content_type='application/json')

        # assert the status code of the response
        self.assertEqual(result.data, b'"Unverified user"')



if __name__ == '__main__':
  unittest.main()
