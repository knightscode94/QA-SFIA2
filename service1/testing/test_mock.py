
import requests
import unittest
from unittest.mock import patch
import requests_mock
  
from flask import url_for
from flask_testing import TestCase
from application import app,db
from application.models import all_data
from os import getenv


class TestBase(TestCase):
    def create_app(self):
        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
                SECRET_KEY=getenv('TEST_SECRET_KEY'),
                WTF_CSRF_ENABLED=False,
                DEBUG=True
                )
        return app

    def setUp(self):
        db.session.commit()
        db.drop_all()
        db.create_all()
        data_record=all_data(question="Will I live a long life?",answer="Sure why not", probability="50% True")

        db.session.add(data_record)
        db.session.commit()


    def tearDown(self):

        db.session.remove()
        db.drop_all()

class TestService1(TestBase):
    def test_home_page(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_generate_ball(self):
            with self.client:
                with requests_mock.Mocker() as m:
                    m.get('http://service2:5001/question', text='"Will I live a long life?')
                    m.get('http://service3:5002/answer', text='Sure why not')
                    m.post('http://service4:5003/probability', text='50% True')                
                    resp = self.client.get(url_for('ball'))
                    self.assertEqual(resp.status_code, 200)