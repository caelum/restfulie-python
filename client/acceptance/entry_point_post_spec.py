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

    def it_follows_201_response_location(self):
        post_uri = 'http://localhost:8081/post_here'
        get_uri = 'http://localhost:8081/myresource'
        self.server_post_response(code=201, location=get_uri)
        self.server_content('<items><item><name>product</name><price>2</price></item></items>',
            'application/xml')
        response = Restfulie.at(post_uri).as_('application/xml').post({'anything': 'goes here'})
        response.items[0].name |should| equal_to('product')
        response.items[0].price |should| equal_to(2)

