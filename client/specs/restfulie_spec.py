# coding: utf-8

import unittest
import urllib2
from ludibrio import Mock, Stub
from should_dsl import should
from restfulie import Restfulie


class RestfulieSpec(unittest.TestCase):

    def setUp(self):
        with Stub() as self._xml_header:
            self._xml_header.gettype() >> 'application/xml'
        with Stub() as self._json_header:
            self._json_header.gettype() >> 'application/json'

    def it_should_retrieve_resource_from_entry_point(self):
        uri = 'http://myrestfulpoweredapp.com/coolresource'
        with Stub() as response:
            response.code >> 200
            response.read() >> 'my restful content'
            response.headers >> {}
        with Stub() as urlopen:
            from urllib2 import urlopen
            urlopen(uri) >> response

        resource = Restfulie.at(uri).raw().get()
        resource.response.code |should| equal_to(200)
        resource.response.body |should| equal_to('my restful content')

    def it_should_allow_xml_retrieval_if_content_type_is_xml(self):
        uri = 'http://myrestfulpoweredapp.com/coolresource'
        with Mock() as response:
            response.code >> 200
            response.read() >> """<person>
                                    <name>Catatau</name>
                                    <address>
                                      <city>Campos dos Goytacazes</city>
                                      <city>Macaé</city>
                                      <city>Rio das Ostras</city>
                                      <state>Rio de Janeiro</state>
                                    </address>
                                  </person>"""
            response.headers >> self._xml_header
        with Stub() as urlopen:
            from urllib2 import urlopen
            urlopen(uri) >> response

        resource = Restfulie.at(uri).get()
        resource.person.name |should| equal_to('Catatau')
        resource.person.address.city |should| equal_to(['Campos dos Goytacazes', u'Macaé', 'Rio das Ostras'])
        resource.person.address.state |should| equal_to('Rio de Janeiro')


    def it_should_allow_json_retrieval_if_content_type_is_application_json(self):
        uri = 'http://myrestfulpoweredapp.com/coolresource'
        with Mock() as response:
            response.code >> 200
            response.read() >> """{"person":{
                                      "name": ["Hugo", "Rodrigo", "Rebeca"],
                                      "address": {
                                            "city": "Campos dos Goytacazes",
                                            "state": "Rio de Janeiro"
                                                 }
                                             }
                                  }"""
            response.headers >> self._json_header
        with Stub() as urlopen:
            from urllib2 import urlopen
            urlopen(uri) >> response

        resource = Restfulie.at(uri).get()
        resource.person.name |should| equal_to(['Hugo', 'Rodrigo', 'Rebeca'])
        resource.person.address.city |should| equal_to('Campos dos Goytacazes')
        resource.person.address.state |should| equal_to('Rio de Janeiro')


