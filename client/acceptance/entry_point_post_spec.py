import unittest
from should_dsl import should
from restfulie import Restfulie
from acceptance_case import RestfulieAcceptanceCase

class EntryPointPost(RestfulieAcceptanceCase):

    def it_posts_as_xml(self):
        content = {'item': {'description': "Black Lantern's t-shirt"}}
        Restfulie.at(self.set_content_uri).as_('application/xml').post(content)
        raw = Restfulie.at(self.content_uri).raw().get()
        raw.response.body |should| equal_to(
            "<item><description>Black Lantern's t-shirt</description></item>")

    def it_posts_as_json(self):
        Restfulie.at(self.set_content_uri).as_('application/json').\
                  post({'some': 'content'})
        raw = Restfulie.at(self.content_uri).raw().get()
        raw.response.body |should| equal_to('{"some": "content"}')

    def it_follows_201_response_location(self):
        self.set_server_post_response(code=201, location=self.content_uri)
        self.set_server_content(
            '<items><item><name>product</name><price>2</price></item></items>',
            'application/xml')
        response = Restfulie.at(self.post_uri).as_('application/xml').\
                             post({'anything': 'goes here'})
        response.items[0].name |should| equal_to('product')
        response.items[0].price |should| equal_to(2)

