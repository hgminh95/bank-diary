from datetime import datetime


def get_array_elem(array, index):
    if index >= len(array):
        return None

    return array[index]


class Transaction(object):

    def __init__(self, *records):
        self.date = get_array_elem(records, 1)
        if isinstance(self.date, str):
            self.date = datetime.strptime(self.date, '%Y%m%d')

        self.statement_code = get_array_elem(records, 2)
        self.reference = get_array_elem(records, 3)
        self.amount = get_array_elem(records, 4)
        self.client_ref = get_array_elem(records, 5)

        # derived attribute
        self.category = 'unknown'
        self.year = self.date.year
        self.month = self.date.month

        self.id = "{}_{}{}_{}_{}".format(
            self.date.strftime('%Y%m%d'),
            self.statement_code,
            self.reference,
            abs(int(self.amount * 100)),
            abs(hash(self.client_ref)) % (10 ** 8))

    def __str__(self):
        return "<T{},{},{},{},{},'{}'>".format(
            self.id,
            self.date.strftime("%Y%m%d"),
            self.statement_code,
            self.reference,
            self.amount,
            self.client_ref
        )

    def __repr__(self):
        return self.__str__()
