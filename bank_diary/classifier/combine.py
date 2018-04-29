class ClassifierSet(object):

    def __init__(self, classifiers):
        self.classifiers = classifiers

    def classify(self, trans):
        res = 'unknown'
        for classifier in self.classifiers:
            res = classifier.classify(trans)
            if res != 'unknown':
                break

        return res
