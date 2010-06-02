"""
adapted from
http://tarekziade.wordpress.com/2010/05/10/faking-a-server-for-client-side-tests/
"""

import threading
import time
from lettuce import *
from wsgiref.simple_server import make_server

def my_resource_app(environ, start_response):
    start_response("200 OK", [('Content-type','application/xml')])
    return ['<item><name>Rich Rock Sunshine</name></item>']


class AppRunner(threading.Thread):
    """Thread that wraps a wsgi app"""

    def __init__(self, wsgiapp):
        threading.Thread.__init__(self)
        self.httpd = make_server('', 8081, wsgiapp)
        self.address = self.httpd.server_address

    def run(self):
        self.httpd.serve_forever()

    def stop(self):
        self.httpd.shutdown()
        time.sleep(0.2)


_SERVER = None

@before.all
def run_server():
    """Runs the server."""
    global _SERVER
    if _SERVER is not None:
        # we suppose it's running
        return _SERVER.address
    _SERVER = AppRunner(my_resource_app)
    _SERVER.start()
    return _SERVER.address

@after.all
def stop_server(total):
    """Stops the server."""
    global _SERVER
    if _SERVER is None:
        return
    _SERVER.stop()
    _SERVER = None

