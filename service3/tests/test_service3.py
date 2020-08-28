from unittest.mock import patch
  
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):

    def create_app(self):
        return app
    def setUp(self):
        pass
    def tearDown(self):
        pass

class TestService2(TestBase):

    def test_questions(self):
        response = self.client.get(url_for('answer'))
        check = False
        for item in ["Not a chance",
            "Sure why not",
            "I mean maybe?"]:
            if bytes.decode(response.data) == item:
                check = True
        self.assertTrue(check)