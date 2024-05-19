# test_routes.py

import unittest
from flask import Flask
from app.routes import flaskApp
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
        # Check for redirection to the gaming page
        self.assertTrue('/game' in response.request.path)

    def test_index_route_login_fail(self):
        # Simulate a POST request to test login failure with incorrect credentials
        response = self.app.post('/', data={'email': 'wrong@example.com', 'password': 'wrong'}, follow_redirects=True)
        # Check that the response does not redirect to the game page
        self.assertFalse('/game' in response.request.path)
        # Ensure the status code is 200, implying that the user stays on the index page
        self.assertEqual(response.status_code, 200)

    def test_logout_route(self):
        # First log in to create a session
        login_response = self.app.post('/', data={'email': 'test@uwa.com', 'password': 'testpass'}, follow_redirects=True)
        # Verify login was successful before testing logout
        self.assertIn('/game', login_response.request.path) 
        # Now attempt to log out
        response = self.app.get('/logout', follow_redirects=True)
        # Check that the user is redirected to the index page
        self.assertEqual(response.status_code, 200)
        self.assertTrue('/' in response.request.path)

if __name__ == '__main__':
    unittest.main()
