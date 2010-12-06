class _Dict2XML(object):

    def convert(self, dictionary):
        output = ""
        for key, value in dictionary.iteritems():
            output += "<%s>" % key
            if isinstance(value, dict):
                output += self.convert(value)
            else:
                output += str(value)
            output += "</%s>" % key
        return output


def dict2xml(dictionary):
    return _Dict2XML().convert(dictionary)

