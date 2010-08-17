from urllib2 import urlopen
from lxml import etree


class Restfulie(object):

    @classmethod
    def at(cls, uri):
        return cls(uri)

    def __init__(self, uri):
        self.response = _Response(urlopen(uri))

    def raw(self):
        return self

    def get(self):
        return self

    def __getattr__(self, attr_name):
        return _ResourceTree(self.response)


class _ResourceTree(object):

    def __init__(self, response):
        self._xml = etree.XML(response.body)

    def __getattr__(self, attr_name):
        return self._xml.find(attr_name).text


class _Response(object):

    def __init__(self, response):
        self.code = response.code
        self.body = response.read()

