class Classifier(object):

    def __init__(self, category, func):
        self.category = category
        self.func = func

    def classify(self, trans):
        return self.category if self.func(trans) else 'unknown'
