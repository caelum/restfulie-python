from urllib2 import urlopen
from lxml import etree
import json


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
        if self._is_xml_resource():
            return _ResourceTreeXML(self.response)
        elif self._is_json_resource():
            return _ResourceTreeJSON(self.response)

    def _is_xml_resource(self):
        return self.response.headers.gettype() in ('application/xml', 'text/xml')

    def _is_json_resource(self):
        return self.response.headers.gettype() == 'application/json'


class _ResourceTreeXML(object):

    def __init__(self, response):
        self._xml = etree.XML(response.body)

    def __getattr__(self, attr_name):
        return self._xml.find(attr_name).text


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
