import unittest
from should_dsl import should
from restfulie import Restfulie
from restfulie import XMLConverter, ConverterRegistry


class dict2xmlSpec(unittest.TestCase):

    def it_converts_flat_dictionary(self):
        dictionary = {'item': {'name': 't-shirt', 'price': 20.0}}
        XMLConverter().marshal(dictionary) |should| be_into([
            '<item><name>t-shirt</name><price>20.0</price></item>',
            '<item><price>20.0</price><name>t-shirt</name></item>'])


class ConverterRegistrySpec(unittest.TestCase):

    def it_registers_converters_by_media_type(self):
        media_type = 'anything'
        converter = 'anything else'
        ConverterRegistry.register(media_type, converter)
        ConverterRegistry.marshaller_for(media_type) |should| be(converter)

