'''
    A simple hello world API
'''
# disabling faulty pylint rules
# pylint:disable=redefined-outer-name

# Standard
from http import HTTPStatus
import logging
from logging.config import dictConfig
import os

# Third Party
from flask import Flask, jsonify, make_response, render_template, request
import yaml

# Local
from src.constants import ContentType

with open('logging-cfg.yml', 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f.read())
    dictConfig(config)

logger = logging.getLogger('app')
dbg = os.environ.get('FLASK_DEBUG', '0')
LOG_LEVEL = logging.DEBUG if os.environ.get('FLASK_DEBUG') == '1' else logging.INFO
logger.setLevel(LOG_LEVEL)

app = Flask(__name__, template_folder='../templates')

@app.route('/', methods=['GET'])
def get_hello():
    '''
    Returns either html or json hello world
    '''
    logger.debug('%s %s', request.method, request.url)
    data = {
        'message': 'Hello, World'
    }
    if _get_accept_header(request) == ContentType.JSON.value:
        return jsonify(data)
    return render_template("index.jinja2", data=data)


@app.route('/', methods=['POST'])
def post_hello():
    '''
    Returns the payload sent
    '''
    logger.debug('%s %s', request.method, request.url)
    data = request.get_json()
    # Instructions were not clear here, thus just logging and returning back the same post payload with status code 201
    response = make_response(jsonify(data), HTTPStatus.CREATED)
    response.headers['Content-type'] = ContentType.JSON.value
    return response

# Private Functions
def _get_accept_header(request):
    accept_header = request.headers.get('Accept', '').lower()
    return accept_header

if __name__ == '__main__':
    DEBUG = True if os.getenv('FLASK_DEBUG') == '1' else False
    PORT = int(os.getenv('FLASK_RUN_PORT', '5000'))
    app.run(debug=DEBUG, port=PORT)
