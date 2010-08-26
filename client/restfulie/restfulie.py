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
        if self._is_raw:
            return self
        if self._is_xml_resource():
            __Result = type('object', (object,), {})
            xml = objectify.fromstring(self.response.body)
            result = __Result()
            setattr(result, xml.tag, MultipleChildrenElement(xml))
            return result
        else: 
            _json = json.loads(self.response.body)
            return _dict2obj(_json)        

    def _is_xml_resource(self):
        return self.response.headers.gettype() in ('application/xml', 'text/xml')

    def _is_json_resource(self):
        return self.response.headers.gettype() == 'application/json'

  
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


class MultipleChildrenElement(object):

    def __init__(self, element):
        self.element = element

    def __getattr__(self, tag):
        tags = self.element.findall(tag)
        if len(tags) > 1:
            return [self.wrap(x) for x in tags]
        else:
            return self.wrap(getattr(self.element, tag))

    def wrap(self, element):
        if element.countchildren():
            return MultipleChildrenElement(element)
        return element
