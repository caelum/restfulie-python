import unittest
from should_dsl import should
from restfulie import Restfulie
from restfulie import XMLConverter, ConverterRegistry, JSONConverter


class XMLConverterSpec(unittest.TestCase):

    def it_marshals_flat_dictionary(self):
        dictionary = {'item': {'name': 't-shirt', 'price': 20.0}}
        XMLConverter().marshal(dictionary) |should| be_into([
            '<item><name>t-shirt</name><price>20.0</price></item>',
            '<item><price>20.0</price><name>t-shirt</name></item>'])

    def it_unmarshals_to_python_objects(self):
        xml = '''<characters>
                   <character>
                     <name>Green Lantern</name>
                     <identity>Hal Jordan</identity>
                   </character>
                   <character>
                     <name>Batman</name>
                     <identity>Dick Grayson</identity>
                   </character>
                   <character>
                     <name>Batgirl</name>
                     <identity>Stephanie Brown</identity>
                   </character>
                 </characters>'''
        result = XMLConverter().unmarshal(xml)
        green_lantern, batman, batgirl = result.characters
        green_lantern.name |should| equal_to('Green Lantern')
        green_lantern.identity |should| equal_to('Hal Jordan')
        batman.name |should| equal_to('Batman')
        batman.identity |should| equal_to('Dick Grayson')
        batgirl.name |should| equal_to('Batgirl')
        batgirl.identity |should| equal_to('Stephanie Brown')


class JSONConverterSpec(unittest.TestCase):

    def it_marshals_flat_dictionary(self):
        dictionary = {'item': {'name': 't-shirt', 'price': 20.0}}
        expected = ['{"item": {"name": "t-shirt", "price": 20.0}}',
                    '{"item": {"price": 20.0, "name": "t-shirt"}}']
        JSONConverter().marshal(dictionary) |should| be_into(expected)


class ConverterRegistrySpec(unittest.TestCase):

    def it_registers_converters_by_media_type(self):
        media_type = 'anything'
        converter = 'anything else'
        ConverterRegistry.register(media_type, converter)
        ConverterRegistry.marshaller_for(media_type) |should| be(converter)

