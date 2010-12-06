import unittest
from should_dsl import should
from restfulie import Restfulie
from restfulie import dict2xml


class dict2xmlSpec(unittest.TestCase):

    def it_converts_flat_dictionary(self):
        dictionary = {'item': {'name': 't-shirt', 'price': 20.0}}
        dict2xml(dictionary) |should| be_into([
            '<item><name>t-shirt</name><price>20.0</price></item>',
            '<item><price>20.0</price><name>t-shirt</name></item>'])

