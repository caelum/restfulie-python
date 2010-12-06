from urllib2 import Request, urlopen
from urllib import urlencode
from converters import ConverterRegistry


class Restfulie(object):

    @classmethod
    def at(cls, uri):
        return cls(uri)

    def __init__(self, uri):
        self._is_raw = False
        self.uri = uri

    def raw(self):
        self._is_raw = True
        return self

    def get(self):
        self.response = _Response(urlopen(self.uri))
        if self._is_raw:
            return self
        else:
            content_type = self.response.headers.gettype()
            return ConverterRegistry.marshaller_for(content_type).\
                unmarshal(self.response.body)

    def as_(self, content_type):
        self._content_type = content_type
        return self

    def post(self, content):
        encoded_content = urlencode({'content':
            ConverterRegistry.marshaller_for(self._content_type).\
                marshal(content)})
        urlopen(self.uri, encoded_content)


class _Response(object):

    def __init__(self, response):
        self.code = response.code
        self.body = response.read()
        self.headers = response.headers

