import json
from lxml import objectify

class ConverterRegistry(object):

    _types = {}

    @classmethod
    def register(cls, type_, converter):
        cls._types[type_] = converter

    @classmethod
    def marshaller_for(cls, type_):
        return cls._types[type_]


class XMLConverter(object):

    def marshal(self, dictionary):
        '''from dictionary'''
        output = ""
        for key, value in dictionary.iteritems():
            output += "<%s>" % key
            if isinstance(value, dict):
                output += self.marshal(value)
            else:
                output += str(value)
            output += "</%s>" % key
        return output

    def unmarshal(self, xml_content):
        '''to object'''
        BlankSlate = type('object', (object,), {})
        result = BlankSlate()
        xml = objectify.fromstring(xml_content)
        child_tag = xml.iterchildren().next().tag
        setattr(result, xml.tag, getattr(xml, child_tag))
        return result


class JSONConverter(object):

    def marshal(self, content):
        '''from dictionary'''
        return json.dumps(content)

    def unmarshal(self, json_content):
        '''to object'''
        return _dict2obj(json.loads(json_content))


class _dict2obj(object):
    '''from: http://stackoverflow.com/questions/1305532/convert-python-dict-to-object'''
    def __init__(self, dict_):
        for key, value in dict_.items():
            if isinstance(value, (list, tuple)):
               setattr(self, key, [_dict2obj(x) if isinstance(x, dict) else x for x in value])
            else:
               setattr(self, key, _dict2obj(value) if isinstance(value, dict) else value)


def _register():
    to_xml, to_json = XMLConverter(), JSONConverter()
    ConverterRegistry.register('text/xml', to_xml)
    ConverterRegistry.register('application/xml', to_xml)
    ConverterRegistry.register('application/json', to_json)

_register()

