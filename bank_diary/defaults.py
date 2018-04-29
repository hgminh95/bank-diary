from bank_diary.classifier import *

classifier = ClassifierSet([
    Classifier('transport', lambda t: t.client_ref == 'EZT'),
    RegexClassifier([
        ('food', 'CHICKEN RICE'),
        ('transport', 'EXPEDIA'),
        ('utility', 'SINGTEL')
    ])
])
