from multiprocessing import Process
from urllib import urlopen
from flask import Flask, request, make_response

app = Flask(__name__)


class Env(object):
    pass
env = Env()
env.content_type = ''
env.process = None
env.host, env.port = 'localhost', 8081


@app.route('/myresource', methods=['GET',])
def myresource():
    response = make_response(env.content)
    response.headers['Content-Type'] = env.content_type
    return response

@app.route('/set_content', methods=['POST',])
def set_content():
    env.content = request.form.get('content')
    return ""

@app.route('/post_here', methods=['POST',])
def post_here():
    response = make_response(env.content, env.post_response_code)
    response.headers['Location'] = env.post_response_location
    return response

@app.route('/set_content_type', methods=['POST',])
def set_content_type():
    env.content_type = request.form.get('content_type')
    return ""

@app.route('/set_post_response', methods=['POST',])
def set_post_response():
    env.post_response_location = request.form.get('location')
    env.post_response_code = int(request.form.get('code'))
    return ""

def start_flask_app(host, port):
    """Runs the server."""
    app.run(host=host, port=port)
    app.config['DEBUG'] = False
    app.config['TESTING'] = False

def wait_until_start():
    while True:
        try:
            urlopen('http://%s:%s' % (env.host, env.port))
            break
        except IOError:
            pass

def wait_until_stop():
    while True:
        try:
            result = urlopen('http://%s:%s' % (env.host, env.port))
            if result.code == 404:
                break
        except IOError:
            break

def start_server():
    env.process = Process(target=start_flask_app, args=(env.host, env.port))
    env.process.daemon = True
    env.process.start()
    wait_until_start()

def stop_server():
    env.process.terminate()
    wait_until_stop()

