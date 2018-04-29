from datetime import datetime


def get_array_elem(array, index):
    if index >= len(array):
        return None

    return array[index]


class Transaction(object):

    def __init__(self, *records):
        self.date = get_array_elem(records, 0)
        if isinstance(self.date, str):
            self.date = datetime.strptime(self.date, '%Y%m%d')

        self.statement_code = get_array_elem(records, 1)
        self.reference = get_array_elem(records, 2)
        self.amount = get_array_elem(records, 3)
        self.client_ref = get_array_elem(records, 4)

    def __str__(self):
        return "<Transaction,{},{},{},{},{}>".format(
            self.date.strftime("%Y%m%d"),
            self.statement_code,
            self.reference,
            self.amount,
            self.client_ref
        )

    def __repr__(self):
        return self.__str__()
