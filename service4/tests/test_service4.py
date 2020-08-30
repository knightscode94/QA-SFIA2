
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

class TestService2(TestBase):

    def test_probability(self):
            with self.client:
                with requests_mock.Mocker() as m:
                    m.get('http://service2:5001/question', text='"Will I live a long life?')
                    m.get('http://service3:5002/answer', text='Sure why not')
                    m.post('http://service4:5003/probability', text='50% True')                
                    response = self.client.get(url_for('probability'))
                    self.assertEqual(response.status_code, 200)