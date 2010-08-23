from urllib2 import urlopen
from lxml import objectify
import json


class Restfulie(object):

    @classmethod
    def at(cls, uri):
        return cls(uri)

    def __init__(self, uri):
        self.response = _Response(urlopen(uri))
        self._is_raw = False

    def raw(self):
        self._is_raw = True
        return self

    def get(self):
        if not self._is_raw and self._is_xml_resource():
            __Result = type('object', (object,), {})
            xml = objectify.fromstring(self.response.body)
            result = __Result()
            setattr(result, xml.tag, xml)
            return result
        return self

    def __getattr__(self, attr_name):
        if self._is_json_resource():
            return _ResourceTreeJSON(self.response)
        return object.__getattr__(self, attr_name)

    def _is_xml_resource(self):
        return self.response.headers.gettype() in ('application/xml', 'text/xml')

    def _is_json_resource(self):
        return self.response.headers.gettype() == 'application/json'


class _ResourceTreeJSON(object):

    def __init__(self, response):
        self._json = json.loads(response.body)

    def __getattr__(self, attr_name):
        return self._find(self._json, attr_name)

    def _find(self, json, attr_name):
        if attr_name in json:
            return json[attr_name]
        for key, value in json.items():
           if isinstance(value, dict):
                result = self._find(value, attr_name)
                if result:
                    return result


class _Response(object):

    def __init__(self, response):
        self.code = response.code
        self.body = response.read()
        self.headers = response.headers

