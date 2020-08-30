
import requests
import unittest
from unittest.mock import patch
import requests_mock
  
from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import all_data
from os import getenv

class TestBase(TestCase):
    def create_app(self):
        return app
    def setUp(self):
        pass
    def tearDown(self):
        pass

class TestService4(TestBase):

    def test_probability(self):
        response = self.client.get(url_for('question'))
        check = False
        for quest in ["Will I ever be good enough at QA?",
                "Is Luke the most epic lecturer at QA?",
                "Will I live a long life?",
                "Is this a load of rubbish?"]:
            if bytes.decode(response.data) == quest:
                check = True
        response = self.client.get(url_for('answer'))
        check = False
        for ans in ["Not a chance",
            "Sure why not",
            "I mean maybe?"]:
            if bytes.decode(response.data) == ans:
                check = True
                
        self.assertTrue(check)