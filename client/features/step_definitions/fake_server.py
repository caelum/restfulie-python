"""
adapted AppRunner thread stuff from:
http://tarekziade.wordpress.com/2010/05/10/faking-a-server-for-client-side-tests/
"""

from multiprocessing import Process
import time
from wsgiref.simple_server import make_server
#from itty import handle_request, get, post, Response
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
#    return Response(data=content, content_type=content_type)
    response = make_response(content)
    response.headers['Content-Type'] = content_type
    return response

@app.route('/set_content', methods=['POST',])
def set_content():
    global content
    content = str(request.data)
    content = '<item><name>Rich Rock Sunshine</name></item>'
    return ""

@app.route('/set_content/type', methods=['POST',])
def set_content_type():
    global content_type
    content_type = str(request.data)
    return ""

def start_flask_app(host, port):
    """Runs the server."""
    app.run(host = '127.0.0.1', port = 8081)

def start_server():
    global _PROCESS, _SERVER, _PORT
    _PROCESS = Process(target=start_flask_app, args=(_SERVER, _PORT))
    _PROCESS.daemon = True
    _PROCESS.start()
    time.sleep(5)

def stop_server():
    global _PROCESS
    _PROCESS.terminate()
    time.sleep(5)

