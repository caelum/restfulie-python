import unittest
import urllib
from should_dsl import should
from fake_server import start_server, stop_server
from restfulie import Restfulie

class EntryPointPost(unittest.TestCase):

    def it_posts_as_xml(self):
        uri = 'http://localhost:8081/set_content'
        content = {'item': {'description': "Black Lantern's t-shirt"}}
        Restfulie.at(uri).as_('application/xml').post(content)

        raw = Restfulie.at('http://localhost:8081/myresource').raw().get()
        raw.response.body |should| equal_to(
            "<item><description>Black Lantern's t-shirt</description></item>")

    def setUp(self):
        start_server()

    def tearDown(self):
        stop_server()

