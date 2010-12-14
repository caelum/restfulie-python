import unittest
import urllib
from should_dsl import should
from fake_server import start_server, stop_server
from restfulie import Restfulie

class EntryPoint(unittest.TestCase):

    def it_gets_raw_data_from_an_entry_point(self):
        uri = 'http://localhost:8081/myresource'
        content = "<item><name>Rich Rock Sunshine</name></item>"
        self.server_content(content)

        resource = Restfulie.at(uri).raw().get()
        resource.response.code |should| be(200)
        resource.response.body |should| equal_to(content)

    def setUp(self):
        start_server()

    def tearDown(self):
        stop_server()

    def server_content(self, content, content_type=None):
        data = urllib.urlencode({'content': content})
        urllib.urlopen('http://localhost:8081/set_content', data)
        if content_type:
            data = urllib.urlencode({'content_type': content_type})
            urllib.urlopen('http://localhost:8081/set_content_type', data)

