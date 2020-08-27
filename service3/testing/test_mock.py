from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_A1(self):
    # We will mock a response of 1 and test
        with patch('requests.get') as g:
            g.return_value.text = "1"

            response = self.client.get(url_for('question'))
            self.assertIn(b'Not a chance', response.data)

    def test_A2(self):
    # We will mock a response of 2 and test
        with patch('requests.get') as g:
            g.return_value.text = "2"

            response = self.client.get(url_for('question'))
            self.assertIn(b'Sure why not', response.data)

    def test_A3(self):
    # We will mock a response of 3 and test
        with patch('requests.get') as g:
            g.return_value.text = "3"

            response = self.client.get(url_for('question'))
            self.assertIn(b'Errrr...', response.data)