import unittest
from app import app

class FlaskBookshelfTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
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
        print(type(result))
        print(type(result.data))
        self.assertEqual(result.data, b'Hello, World!')


    # def test_isVerified(self):
    #     # sends HTTP GET request to the application
    #     # on the specified path
    #     # result = self.app.post('/isVerified', )
    #
    #     # assert the status code of the response
    #     self.assertEqual(result.status_code, 200)
    #     self.assertEqual(result.value, True)


        # { "code": 3882, "phone": "2014563334" }

if __name__ == '__main__':
  unittest.main()
