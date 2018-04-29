import re


class RegexClassifier(object):

    def __init__(self, patterns):
        self.patterns = patterns

    def classify(self, trans):
        for key, regex in self.patterns:
            if re.search(regex, trans.client_ref) is not None:
                return key
        return 'unknown'
