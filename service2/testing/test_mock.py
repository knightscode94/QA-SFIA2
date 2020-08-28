from unittest.mock import patch
  
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):

    def create_app(self):
        config_name = 'testing'
        return app
    def setUp(self):
        pass
    def tearDown(self):
        pass

class TestService2(TestBase):

    def test_questions(self):
        response = self.client.get(url_for('question'))
        check = False
        for item in ["Will I ever be good enough at QA?",
                "Is Luke the most epic lecturer at QA?",
                "Will I live a long life?",
                "Is this a load of rubbish?"]:
            if bytes.decode(response.data) == item:
                check = True
        self.assertTrue(check)