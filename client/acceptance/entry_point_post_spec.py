import unittest
from should_dsl import should
from restfulie import Restfulie
from acceptance_case import RestfulieAcceptanceCase

class EntryPointPost(RestfulieAcceptanceCase):

    def it_posts_as_xml(self):
        uri = 'http://localhost:8081/set_content'
        content = {'item': {'description': "Black Lantern's t-shirt"}}
        Restfulie.at(uri).as_('application/xml').post(content)

        raw = Restfulie.at('http://localhost:8081/myresource').raw().get()
        raw.response.body |should| equal_to(
            "<item><description>Black Lantern's t-shirt</description></item>")

    def it_posts_as_json(self):
        uri = 'http://localhost:8081/set_content'
        Restfulie.at(uri).as_('application/json').post({'some': 'content'})

        raw = Restfulie.at('http://localhost:8081/myresource').raw().get()
        raw.response.body |should| equal_to('{"some": "content"}')

