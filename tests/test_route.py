# test_routes.py

import unittest
from flask import Flask
from app.routes import flaskApp  # Adjust the import according to your actual application structure
from app import db

class TestIndexRoute(unittest.TestCase):

    def setUp(self):
        self.app = flaskApp.test_client()
        self.app.testing = True
        flaskApp.config['WTF_CSRF_ENABLED'] = False

    def test_index_route_login(self):
        # Simulate a POST request to test login
        response = self.app.post('/', data={'email': 'test@uwa.com', 'password': 'testpass'}, follow_redirects=True)
        # Check for redirection status code
        self.assertEqual(response.status_code, 200)
        # Optionally check for redirection to a specific endpoint
        self.assertTrue('/game' in response.request.path)

    # def test_index_route_login_fail(self):
    #     # Simulate a POST request to test login failure
    #     response = self.app.post('/', data={'email': 'wrong@example.com', 'password': 'wrong'}, follow_redirects=True)
    #     # Check for login fail response
    #     self.assertIn('Invalid email or password', response.data.decode('utf-8'))
    #     self.assertEqual(response.status_code, 200)  # Assuming the page reloads on failure

if __name__ == '__main__':
    unittest.main()
