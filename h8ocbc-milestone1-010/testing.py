from app import connex_app
import unittest

class FlaskTestCase(unittest.TestCase):
    
    """
    This function if for testing will the /api/director/ sends a 200 response or not
    """
    def test_get_all_directors(self):
        connex_app.app.testing = True
        tester = connex_app.app.test_client(self)
        response = tester.get('/api/director')
        self.assertEqual(response.status_code, 200)

    """
    This function if for testing will the /api/movie/ sends a 200 response or not
    """
    def test_get_all_movies(self):
        connex_app.app.testing = True
        tester = connex_app.app.test_client(self)
        response = tester.get('/api/movie')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()