from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_Q1(self):
    # We will mock a response of 1 and test
        with patch('requests.get') as g:
            g.return_value.text = "1"

            response = self.client.get(url_for('question'))
            self.assertIn(b'Will I ever be good enough at QA?', response.data)

    def test_Q2(self):
    # We will mock a response of 2 and test
        with patch('requests.get') as g:
            g.return_value.text = "2"

            response = self.client.get(url_for('question'))
            self.assertIn(b'Is Luke the most epic lecturer at QA?', response.data)

    def test_Q3(self):
    # We will mock a response of 3 and test
        with patch('requests.get') as g:
            g.return_value.text = "3"

            response = self.client.get(url_for('question'))
            self.assertIn(b'Will I live a long life?', response.data)

    def test_Q4(self):
    # We will mock a response of 4 and test
        with patch('requests.get') as g:
            g.return_value.text = "4"

            response = self.client.get(url_for('question'))
            self.assertIn(b'Is this a load of rubbish?', response.data)