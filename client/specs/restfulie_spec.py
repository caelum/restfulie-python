import unittest
import urllib2
from ludibrio import Stub
from should_dsl import should
from restfulie import Restfulie


class RestfulieSpec(unittest.TestCase):

    def it_should_retrieve_resource_from_entry_point(self):
        uri = 'http://myrestfulpoweredapp.com/coolresource'
        with Stub() as response:
            response.code = 200
            response.read() >> 'my restful content'
        with Stub() as urlopen:
            from urllib2 import urlopen
            urlopen(uri) >> response

        resource = Restfulie.at(uri).raw().get()
        resource.response.code |should| equal_to(200)
        resource.response.body |should| equal_to('my restful content')

