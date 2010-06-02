from urllib2 import urlopen


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


class _Response(object):
    def __init__(self, response):
        self.code = response.code
        self.body = response.read()

