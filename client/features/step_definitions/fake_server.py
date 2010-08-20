"""
adapted AppRunner thread stuff from:
http://tarekziade.wordpress.com/2010/05/10/faking-a-server-for-client-side-tests/
"""

import threading
import time
from wsgiref.simple_server import make_server
from itty import handle_request, get, post, Response


_SERVER = None
_HOST, _PORT = 'localhost', 8081

content = ""
content_type = ""

@get('/myresource')
def myresource(web):
    return Response(content, content_type=content_type)

@post('/set_content')
def set_content(request):
    global content
    content = request.POST.get('content', '')
    return ""

@post('/set_content_type')
def set_content_type(request):
    global content_type
    content_type = request.POST.get('content_type', '')
    return ""


class AppRunner(threading.Thread):
    """Thread that wraps a wsgi app"""

    def __init__(self, wsgiapp):
        threading.Thread.__init__(self)
        self.httpd = make_server(_HOST, _PORT, wsgiapp)
        self.address = self.httpd.server_address

    def run(self):
        self.httpd.serve_forever()

    def stop(self):
        self.httpd.shutdown()


def start_server():
    """Runs the server."""
    global _SERVER
    if _SERVER is not None:
        # we suppose it's running
        return _SERVER.address
    _SERVER = AppRunner(handle_request)
    _SERVER.start()
    return _SERVER.address


def stop_server():
    """Stops the server."""
    global _SERVER
    if _SERVER is None:
        return
    _SERVER.stop()
    _SERVER = None

