"""
adapted AppRunner thread stuff from:
http://tarekziade.wordpress.com/2010/05/10/faking-a-server-for-client-side-tests/
"""

import threading
import time
from wsgiref.simple_server import make_server
from juno import config, get, content_type, run


_SERVER = None
_HOST, _PORT = 'localhost', 8081

config({'mode': 'wsgi',
        'use_templates': False,
        'template_lib': None,
        'use_static': False,
        'use_db': False,
        'log': False})


@get('/myresource')
def myresource(web):
    content_type('application/xml')
    return '<item><name>Rich Rock Sunshine</name></item>'


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
    juno_app = run()
    _SERVER = AppRunner(juno_app)
    _SERVER.start()
    return _SERVER.address


def stop_server():
    """Stops the server."""
    global _SERVER
    if _SERVER is None:
        return
    _SERVER.stop()
    _SERVER = None
