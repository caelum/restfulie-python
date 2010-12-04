"""
adapted AppRunner thread stuff from:
http://tarekziade.wordpress.com/2010/05/10/faking-a-server-for-client-side-tests/
"""

from multiprocessing import Process
import urllib
import time
from wsgiref.simple_server import make_server
from flask import Flask, request, make_response

app = Flask(__name__)


_PROCESS = None
_SERVER = None
_HOST, _PORT = 'localhost', 8081

content = ""
content_type = ""

@app.route('/myresource', methods=['GET',])
def myresource():
    global content
    global content_type
    response = make_response(content)
    response.headers['Content-Type'] = content_type
    return response

@app.route('/set_content', methods=['POST',])
def set_content():
    global content
    content = request.form.get('content')
    return ""

@app.route('/set_content_type', methods=['POST',])
def set_content_type():
    global content_type
    content_type = request.form.get('content_type')
    return ""

def start_flask_app(host, port):
    """Runs the server."""
    app.run(host = '127.0.0.1', port = 8081)
    app.config['DEBUG'] = False
    app.config['TESTING'] = False

def wait_until_start():
    while True:
        try:
            urllib.urlopen('http://%s:%s' % (_HOST, _PORT))
            break
        except IOError:
            pass

def wait_until_stop():
    while True:
        try:
            result = urllib.urlopen('http://%s:%s' % (_HOST, _PORT))
            if result.code == 404:
                break
        except IOError:
            break

def start_server():
    global _PROCESS, _SERVER, _PORT
    _PROCESS = Process(target=start_flask_app, args=(_SERVER, _PORT))
    _PROCESS.daemon = True
    _PROCESS.start()
    wait_until_start()

def stop_server():
    global _PROCESS
    _PROCESS.terminate()
    wait_until_stop()

