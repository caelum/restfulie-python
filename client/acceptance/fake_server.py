from multiprocessing import Process
from urllib import urlopen
from flask import Flask, request, make_response

app = Flask(__name__)


_PROCESS = None
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
    if 'redirect_to' in content:
        url_to_go = content.split()[1]
        response = make_response(content, 201)
        response.headers['Location'] = url_to_go
    else:
        response = make_response(content)
    return response

@app.route('/set_content_type', methods=['POST',])
def set_content_type():
    global content_type
    content_type = request.form.get('content_type')
    return ""

def start_flask_app(host, port):
    """Runs the server."""
    app.run(host = host, port = port)
    app.config['DEBUG'] = False
    app.config['TESTING'] = False

def wait_until_start():
    while True:
        try:
            urlopen('http://%s:%s' % (_HOST, _PORT))
            break
        except IOError:
            pass

def wait_until_stop():
    while True:
        try:
            result = urlopen('http://%s:%s' % (_HOST, _PORT))
            if result.code == 404:
                break
        except IOError:
            break

def start_server():
    global _PROCESS, _PORT
    _PROCESS = Process(target=start_flask_app, args=(_HOST, _PORT))
    _PROCESS.daemon = True
    _PROCESS.start()
    wait_until_start()

def stop_server():
    global _PROCESS
    _PROCESS.terminate()
    wait_until_stop()

