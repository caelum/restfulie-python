from urllib2 import Request, urlopen
from urllib import urlencode
from lxml import objectify
import json

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
        if self._is_xml_resource():
            BlankSlate = type('object', (object,), {})
            result = BlankSlate()
            xml = objectify.fromstring(self.response.body)
            child_tag = xml.iterchildren().next().tag
            setattr(result, xml.tag, getattr(xml, child_tag))
            return result
        else:
            _json = json.loads(self.response.body)
            return _dict2obj(_json)

    def _is_xml_resource(self):
        return self.response.headers.gettype() in ('application/xml', 'text/xml')

    def _is_json_resource(self):
        return self.response.headers.gettype() == 'application/json'

    def as_(self, content_type):
        return self

    def post(self, content):
        encoded_content = urlencode({'content': content})
        urlopen(self.uri, encoded_content)


class _dict2obj(object):
    '''from: http://stackoverflow.com/questions/1305532/convert-python-dict-to-object'''
    def __init__(self, dict_):
        for key, value in dict_.items():
            if isinstance(value, (list, tuple)):
               setattr(self, key, [_dict2obj(x) if isinstance(x, dict) else x for x in value])
            else:
               setattr(self, key, _dict2obj(value) if isinstance(value, dict) else value)


class _Response(object):

    def __init__(self, response):
        self.code = response.code
        self.body = response.read()
        self.headers = response.headers

