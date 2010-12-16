import unittest
from should_dsl import should
from restfulie import Restfulie
from acceptance_case import RestfulieAcceptanceCase

class EntryPoint(RestfulieAcceptanceCase):

    def it_gets_raw_data_from_an_entry_point(self):
        content = "<item><name>Rich Rock Sunshine</name></item>"
        self.set_server_content(content)

        resource = Restfulie.at(self.content_uri).raw().get()
        resource.response.code |should| be(200)
        resource.response.body |should| equal_to(content)

    def it_retrieves_content_as_xml(self):
        content = '''<items>
                        <item>
                            <name>product</name>
                            <price>2</price>
                        </item>
                        <item>
                            <name>another product</name>
                            <price>5</price>
                        </item>
                    </items>'''

        for content_type in ('application/xml', 'text/xml'):
            self.set_server_content(content, content_type)

            resource = Restfulie.at(self.content_uri).get()
            resource.items[0].name |should| equal_to('product')
            resource.items[0].price |should| be(2)
            resource.items[1].name |should| equal_to('another product')
            resource.items[1].price |should| be(5)

    def it_retrieves_content_as_json(self):
        content = '''{"item": {"name": "product", "price": 2}}'''
        self.set_server_content(content, 'application/json')

        resource = Restfulie.at(self.content_uri).get()
        resource.item.name |should| equal_to('product')
        resource.item.price |should| be(2)

