import unittest
from flask import Flask
from app.routes import flaskApp
from app import db

class TestIndexRoute(unittest.TestCase):

    def setUp(self):
        self.app = flaskApp.test_client()
        self.app.testing = True
        flaskApp.config['WTF_CSRF_ENABLED'] = False

    # Test Case 1: Test a user successfully login the account
    def test_index_route_login(self):
        response = self.app.post('/', data={'email': 'test@uwa.com', 'password': 'testpass'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('/menu' in response.request.path)

    # Test Case 2: Test a user failed to login the account
    def test_index_route_login_fail(self):
        response = self.app.post('/', data={'email': 'wrong@example.com', 'password': 'wrong'}, follow_redirects=True)
        self.assertFalse('/game' in response.request.path)
        self.assertEqual(response.status_code, 200)

    # Test Case 3: Test a user successfully to logout the account
    def test_logout_route(self):
        login_response = self.app.post('/', data={'email': 'test@uwa.com', 'password': 'testpass'}, follow_redirects=True)
        self.assertIn('/menu', login_response.request.path)
        response = self.app.get('/logout', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('/' in response.request.path)

    # Test Case 4: Test a user successfully to access the create theme page
    def test_access_create_page(self):
        self.login()
        response = self.app.get('/create', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # Test Case 5: Test a user successfully to access the leaderboard page
    def test_access_leaderboard_page(self):
        self.login()
        response = self.app.get('/leaderboard', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # Test Case 6: Test a user successfully to access the profile page
    def test_access_profile_page(self):
        self.login()
        response = self.app.get('/profile', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # Helper method to log in
    def login(self):
        return self.app.post('/', data={'email': 'test@uwa.com', 'password': 'testpass'}, follow_redirects=True)

if __name__ == '__main__':
    unittest.main()
