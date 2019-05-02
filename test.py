import unittest

from app.server import app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_hello_world(self):
        res = self.app.get('/')
        self.assertEqual(res.status_code, 200)
        self.assertIn('Hello World!', str(res.data))

if __name__ == "__main__":
    unittest.main()
