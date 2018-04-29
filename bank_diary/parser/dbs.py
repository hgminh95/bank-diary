from datetime import datetime

from .base import BaseParser
from bank_diary.common.models import Transaction


class DbsParser(BaseParser):

    _name = 'dbs'

    def __init__(self):
        pass

    def parse_file(self, path):
        with open(path, 'rt') as f:
            in_data_area = False
            for line in f:
                if "Transaction Date" in line:
                    in_data_area = True
                    continue

                if not in_data_area:
                    continue

                tokens = line.replace('\n', '').split(",")
                if len(tokens) < 10:
                    continue

                yield self.parse_line(tokens)

    def parse_line(self, tokens):
        t = Transaction()
        t.date = datetime.strptime(tokens[0], "%d %b %Y")
        t.statement_code = tokens[2]
        t.reference = tokens[3]
        if tokens[4] != " ":
            t.amount = float(tokens[4])
        else:
            t.amount = 0
        t.client_ref = tokens[6]

        return t
