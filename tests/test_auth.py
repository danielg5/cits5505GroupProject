import unittest
from app import create_app
from app.config import Config

class TestConfig(Config):
    TESTING = True
    SECRET_KEY = 'test-secret'

class AuthTestCase(unittest.TestCase):

    def setUp(self):
        """Set up test variables."""
        self.app = create_app(TestConfig)
        self.client = self.app.test_client()

    def test_login_page(self):
        """Test the login page."""
        response = self.client.get('/auth/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Login Page', response.get_data(as_text=True))

    def test_logout_page(self):
        """Test the logout page."""
        response = self.client.get('/auth/logout')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Logout Page', response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()
