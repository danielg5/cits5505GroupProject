import unittest
from flask import Flask, session
from app.routes import flaskApp
from app import db

class TestIndexRoute(unittest.TestCase):

    def setUp(self):
        self.app = flaskApp.test_client()
        self.app.testing = True
        flaskApp.config['WTF_CSRF_ENABLED'] = False
        flaskApp.config['SECRET_KEY'] = 'mysecret'

    def test_index_route_login(self):
        # Simulate a POST request to test login
        response = self.app.post('/', data={'email': 'test@uwa.com', 'password': 'testpass'}, follow_redirects=True)
        # Check for redirection status code
        self.assertEqual(response.status_code, 200)
        # Check for expected content indicating redirection to the game page
        self.assertIn('Game Page', response.data.decode())

    def test_index_route_login_fail(self):
        # Simulate a POST request to test login failure with incorrect credentials
        response = self.app.post('/', data={'email': 'wrong@example.com', 'password': 'wrong'}, follow_redirects=True)
        # Check that the response does not redirect to the game page
        self.assertNotIn('Game Page', response.data.decode())
        # Ensure the status code is 200, implying that the user stays on the index page
        self.assertEqual(response.status_code, 200)

    def test_logout_route(self):
        # First log in to create a session
        self.app.post('/', data={'email': 'test@uwa.com', 'password': 'testpass'}, follow_redirects=True)
        # Now attempt to log out
        response = self.app.get('/logout', follow_redirects=True)
        # Check that the user is redirected to the index page
        self.assertEqual(response.status_code, 200)
        self.assertIn('Login Page', response.data.decode())  # Assuming the index page has "Login Page" text

if __name__ == '__main__':
    unittest.main()
