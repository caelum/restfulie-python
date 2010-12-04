# coding: utf-8

import unittest
import urllib2
from ludibrio import Mock, Stub, Dummy
from should_dsl import should
from restfulie import Restfulie


class EntryPointPostSpec(unittest.TestCase):
    def it_should_allow_posting_as_xml(self):
        uri = 'http://coolresource/post-here'
        content = 'some content'
        encoded_content = Dummy()
        with Mock() as urlencode:
            from urllib import urlencode
            urlencode({'content': content}) >> encoded_content
        with Mock() as urlopen:
            from urllib2 import urlopen
            urlopen(uri, encoded_content)
        Restfulie.at(uri).as_('application/xml').post(content)
        urlencode.validate()
        urlopen.validate()

    def it_should_allow_posting_as_json(self):
        uri = 'http://coolresource/post-here'
        content = {"just":"testing"}
        encoded_content = Dummy()
        with Mock() as dumps:
            from json import dumps
            dumps(content) >> encoded_content
        with Mock() as urlopen:
            from urllib2 import urlopen
            urlopen(uri, encoded_content)
        Restfulie.at(uri).as_('application/json').post(content)
        urlopen.validate()
        dumps.validate()

