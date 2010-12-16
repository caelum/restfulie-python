import unittest
import urllib
from fake_server import start_server, stop_server

class RestfulieAcceptanceCase(unittest.TestCase):
    '''For info about URIs below, please see fake_server.py'''

    set_content_uri = 'http://localhost:8081/set_content'
    content_uri = 'http://localhost:8081/myresource'
    post_uri = 'http://localhost:8081/post_here'

    def setUp(self):
        start_server()

    def tearDown(self):
        stop_server()

    def set_server_content(self, content, content_type=None):
        data = urllib.urlencode({'content': content})
        urllib.urlopen('http://localhost:8081/set_content', data)
        if content_type:
            data = urllib.urlencode({'content_type': content_type})
            urllib.urlopen('http://localhost:8081/set_content_type', data)

    def set_server_post_response(self, code, location):
        data = urllib.urlencode({'code': code, 'location': location})
        urllib.urlopen('http://localhost:8081/set_post_response', data)

