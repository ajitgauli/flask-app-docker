'''
    Unit tests for app.py endpoints.
'''

# pylint:disable=missing-class-docstring,missing-function-docstring,no-member,no-self-use
from flask import json
from flask_testing import TestCase

from src.app import app

class AppTest(TestCase):
    def create_app(self):
        # app = Flask(__name__)
        app.config['testing'] = True
        return app

    def test_get(self):
        with app.test_client() as tcl:
            resp = tcl.get('/')
            data = resp.get_data(as_text=True)
            self.assert_template_used('index.jinja2')
            data = {'message': 'Hello, World'}
            self.assert_context('data', data)

    def test_get_with_json_accept_header(self):
        with app.test_client() as tcl:
            resp = tcl.get('/', headers={'Accept': 'application/json'})
            data = json.loads(resp.get_data(as_text=True))
            assert resp.status_code == 200
            assert data == {'message': 'Hello, World'}

    def test_post(self):
        with app.test_client() as tcl:
            msg = {'message': 'Bonjour'}
            resp = tcl.post(
                '/',
                data=json.dumps(msg),
                headers={'content-type': 'application/json'}
            )
            data = json.loads(resp.get_data(as_text=True))
            assert resp.status_code == 201
            assert data == msg
